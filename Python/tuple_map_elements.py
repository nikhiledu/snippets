#!/usr/bin/python
default_repos_immutable_tuples = ("outage-ggg",
                 "service-ggg-config",
                 "grafana-dashboards",
                 "kibana-dashboards",

                 "jenkins-config")

default_repos_dict = {"outage-ggg",
                 "service-ggg-config",
                 "grafana-dashboards",
                 "kibana-dashboards",

                 "jenkins-config"}

print("default_repos_immutable_tuples: {}".format(default_repos_immutable_tuples))
print("default_repos_dict: {}".format(default_repos_dict))

for i in default_repos_immutable_tuples:
  print("Element: {} {}".format(type(i), i))

for i in default_repos_dict:
  print("Element: {} {}".format(type(i), i))

