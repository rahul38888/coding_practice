from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(chunk_size=600,
                                               chunk_overlap=100)

if __name__ == '__main__':
    text = ("Cassandra Cluster Setup\nOne Liner:\nIn this project I created a "
            "multi-datacentre Cassandra Cluster to fix multiple issues and "
            "increase system availability from 98% to 99.99%\nPara:\nSo, "
            "the Cassandra cluster they had in place contained single "
            "datacentre and was prone to infrastructure failure. Furthermore, "
            "there was no observability and no data backup. Also, in case of "
            "high read load, write application would get affected. All these "
            "problems led to low availability of 98% of our read and write "
            "applications.\nAs my first project I was assigned the task to "
            "setup a cluster which would solves these problems. So, I did "
            "three things\n-	First, I changed Replication strategy from "
            "Simple Strategy to Network Topology Strategy. This solved rack "
            "or datacentre failure issue.\n-	Second, to have two "
            "datacentres, one for read traffic and another for write traffic. "
            "This eliminated the effect of high read load on write "
            "application.\n-	Third, I also introduced DR setup, backup "
            "strategy, real time monitoring and alerting system for "
            "observability.\n-	And finally, before handing over this project"
            " to DevOps, I automated node recovery and data repair.\nThe "
            "impact of this was a higher fault tolerance, low latency, data "
            "consistency and traffic load separation. And our system "
            "availability improved to 99.99 %.\nChallenges\nThe main "
            "challenge was in the POC itself. Because I was the only person "
            "in the team and was not well versed with Cassandra. As you know, "
            "Cassandra has a steep learning curve as well. But yeah, I gave "
            "in extra hours to learning and my manager was also very "
            "supportive, so to be honest I enjoyed it. And yeah, once I had "
            "the hang of Cassandra, it was easy to formulate a solution.")

    strings = text_splitter.split_text(text)

    for s in strings:
        print(f"-- {len(s)} ---\t{s}")