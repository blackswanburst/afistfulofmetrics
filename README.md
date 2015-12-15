This repository is for a variety of code dedicated to metrics for "cyber risk" or infosec and hacking as I know it.

The goal is to provide some useful tools and extensions to cyber risk metricians and quants.

The Leverett-Wightman-cost was a simple idea invented with Reid Wightman while scanning the internet looking for vulnerable Programmable Logics Controllers. The paper can be found here if that interests you...

http://grehack.org/files/2013/GreHack_2013_proceedings-separate_files/3-accepted_papers/3.6_E_Leverett_and_Reid_Wightman_-_Vulnerability_Inheritance_in_Programmable_Logic_Controllers.pdf

However, the idea itself is simple metric to help measure the DISTRIBUTION of a vulnerability across an address space. Essentially, vulnerability at scale. The code is a simple proof of concept for others to experiment with the metric, and expand upon the ideas.

Example query (CVE-2015-5377):

'port:9200 +"You Know, for Search" -2.0.0 -1.6.2 -1.7.3 -1.7.2 -1.7.1 -1.7.0 -1.6.1 -503'

https://asciinema.org/a/27926
Example query (John Matherly's most extensive SSH key fingerprint):
'e7:86:c7:22:b3:08:af:c7:11:fb:a5:ff:9a:ae:38:e4'
