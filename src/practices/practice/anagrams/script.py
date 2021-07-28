# https://practice.geeksforgeeks.org/problems/print-anagrams-together/1

def merge(word, s, m, e):
    l = list(word)
    i = s
    j = m + 1
    st = []
    while i <= m and j <= e:
        if l[i] < l[j]:
            st.append(l[i])
            i += 1
        else:
            st.append(l[j])
            j += 1
    while i <= m:
        st.append(l[i])
        i += 1
    while j <= e:
        st.append(l[j])
        j += 1
    l[s:e + 1] = st
    return "".join(l)


def sortString(word, s, e):
    if s >= e:
        return word
    m = int((s + e) / 2)
    word = sortString(word, s, m)
    word = sortString(word, m + 1, e)
    return merge(word, s, m, e)


def Anagrams(words, n):
    sorted_words = [0] * n
    for i in range(n):
        sorted_words[i] = sortString(words[i], 0, len(words[i]) - 1)

    groups_map = {}
    for i in range(n):
        if not groups_map.__contains__(sorted_words[i]):
            groups_map[sorted_words[i]] = []
        groups_map.get(sorted_words[i]).append(words[i])
    return groups_map.values()


if __name__ == '__main__':
    t = int(input())
    for tcs in range(t):
        n = int(input())
        words = input().split()

        ans = Anagrams(words, n)

        for grp in sorted(ans):
            for word in grp:
                print(word, end=' ')
            print()
