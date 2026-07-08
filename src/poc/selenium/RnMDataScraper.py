from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import datetime

start_url = "https://rickandmorty.fandom.com/wiki/Pilot/Transcript"

chrome_options = Options()
chrome_options.add_experimental_option(
    "prefs", {'profile.managed_default_content_settings.javascript': 2})
driver = webdriver.Chrome(options=chrome_options)


def get_session_name() -> str:
    # .page-header__categories a[data-tracking-label="categories-top-more-1"]
    session_name = (driver.find_element(by=By.CLASS_NAME,
                                        value='page-header__categories')
                    .find_elements(by=By.TAG_NAME, value="a")[-1].text)
    return (session_name.replace("transcripts", "")
            .strip())


def get_episode_name() -> str:
    episode_name = driver.find_element(by=By.CLASS_NAME,
                                       value="mw-page-title-main").text
    return episode_name.split("/")[0]


def get_transcript_text() -> str:
    # .mw-parser-output
    t_outer_html = driver.find_element(by=By.CLASS_NAME,
                                       value="mw-parser-output")
    try:
        transcript_html = t_outer_html.find_element(by=By.CLASS_NAME,
                                                    value="poem")
        return transcript_html.text
    except NoSuchElementException:
        transcript_texts = []
        transcript_html = t_outer_html.find_elements(by=By.TAG_NAME, value="p")
        for i in range(1, len(transcript_html)):
            transcript_texts.append(transcript_html[i].text)
        return "\n".join(transcript_texts)


def get_next_link():
    try:
        next_link = (driver.find_elements(by=By.CLASS_NAME, value="Userbox")[1]
                     .find_element(by=By.TAG_NAME, value='tbody')
                     .find_element(by=By.TAG_NAME, value='tr')
                     .find_elements(by=By.TAG_NAME, value='td')[1]
                     .find_element(by=By.TAG_NAME, value='a'))
        href = next_link.get_property('href')
        link_name = next_link.text
        return href, link_name
    except NoSuchElementException:
        return None, None


def get_all_episodes_urls():
    driver.get(start_url)
    result = {"Season 1": {"Pilot": start_url}}
    trs = (driver.find_element(value="infobox-interior", by=By.CLASS_NAME)
           .find_elements(by=By.TAG_NAME, value="tr"))[2:]

    for tr in trs:
        session = tr.find_element(by=By.TAG_NAME, value="th").text
        if session not in result:
            result[session] = {}
        bs = (tr.find_element(by=By.TAG_NAME, value="td")
              .find_elements(by=By.TAG_NAME, value="b"))
        for b in bs:
            try:
                a = b.find_element(by=By.TAG_NAME, value="a")
                episode_name = a.text
                href = a.get_property('href')
            except NoSuchElementException:
                episode_name = b.text
                href = ""

            if episode_name not in result[session]:
                result[session][episode_name] = href

    return result


def normalize_series_info(data: dict[str, dict[str, str]]):
    si_df = pd.DataFrame(columns=["Index", "Session", "Episode", "Url"])
    eindex = 0
    for s in data:
        for e in data[s]:
            eu = data[s][e]
            si_df.loc[len(si_df)] = (eindex, s, e, eu)
            eindex += 1

    return si_df


if __name__ == '__main__':
    now = datetime.datetime.now()
    date_text = f"{now.year}-{now.month}-{now.day}_{now.hour}-{now.minute}-{now.second}"

    url = start_url
    name = "Pilot"
    df = pd.DataFrame(columns=
                      ["Index", "Session", "Episode", "Transcript", "Source"])

    series_info = get_all_episodes_urls()

    si = normalize_series_info(series_info)
    si.to_excel(f"data/RnM_Sources-{date_text}.xlsx",
                sheet_name="Sources")

    for index in range(len(si)):
        episode = si.iloc[index]

        e_index = episode["Index"]
        session_name = episode["Session"]
        episode_name = episode["Episode"]
        url = episode["Url"]

        if url == "":
            print(f"No valid url found for {episode_name}. SKIPPING ----------")
            transcript_text = ""
        else:
            print("Scraped data for",
                  (e_index, session_name, episode_name, url))

            driver.get(url)
            driver.implicitly_wait(1.0)
            transcript_text = get_transcript_text()

        df.loc[len(df)] = (e_index, session_name,
                           episode_name, transcript_text, url)

    df.to_excel(f"data/RnM_Transcripts-{date_text}.xlsx",
                sheet_name="Transcripts")
