# DefendICS (pronounced defendix)

This project is a collection of tools, scripts and data catalogs and other useful information focused on security hardening in critical infrastructure. 

Our belief is that this is a critical, but missing, capability for security misconfiguration efficacy and prioritization.

The initial release includes the only known implementation of a CCSS (Common Configuration Scoring System) python script [ccss.py](https://github.com/opswright-labs/defendics/blob/main/ccss.py) severity scoring tool conformant with the [proposed CCSS approach by NIST](https://www.nist.gov/publications/common-configuration-scoring-system-ccss-metrics-software-security-configuration). While we don't believe that this is any better than CVSS, it's one of the only quantifiable methods documented today. And this precisely is what we will be working on in future releases of defendics.

For information on how we are approaching this topic, check out the articles on security hardening at [opswright.com](https://www.opswright.com/topic/security-hardening). The idea is to create a model for prioritization, similar to [EPSS](https://www.first.org/epss/) to establish control efficacy in a measurable and threat-informed way. We already use EPSS and KEV in our vulnerability prioritization, so a similar approach is attractive to us, yet we are in a feasibility analysis stage to determine if this is even realistic. 

**EPSS Methodology**

EPSS utilizes the following aspects, and these, along with other useful data mapping from industry, is what guides our efforts:

*	Vendor (CPE, via NVD) - Identifies the vendor of the product affected by the vulnerability.
* Age of the Vulnerability - Considers how long a vulnerability has been known since its publication in the MITRE CVE list.
* References with Categorical Labels - Uses sources like the MITRE CVE List and NVD for detailed vulnerability descriptions.
* Normalized Multiword Expressions - Extracts terms from the vulnerability description that help in understanding the vulnerability context.
* Weakness in the Vulnerability (CWE) - Classifies the type of software weakness the vulnerability represents.
* CVSS Metrics - Provides a standardized score to reflect the severity of the vulnerability.
* CVE Discussion Lists/Websites - Tracks whether the vulnerability is being actively discussed in security communities or listed on key vulnerability sites.
* Publicly Available Exploit Code - Indicates if exploit code is available in repositories like Exploit-DB, GitHub, or tools like MetaSploit.
* Offensive Security Tools and Scanners - Lists tools that could potentially be used to exploit the vulnerability.

**Other Useful Links**

* [Awesome Security Hardening](https://github.com/decalage2/awesome-security-hardening) at GitHub
* [Awesome Industrial Control Systems Security](https://github.com/hslatman/awesome-industrial-control-system-security) at GitHub
* [Cross-sector Cybersecurity Performance Goals (CPG)](https://www.cisa.gov/cross-sector-cybersecurity-performance-goals) from CISA

**Data Sources**

* https://ncp.nist.gov/cce
* https://ncp.nist.gov/repository
* https://github.com/usnistgov/oscal-content/tree/main


**Data Specifications**

These are some of the structured data sources that we are getting into. We have a draft JSON specification that is aligned with all three standards and a working python script to ingest CCE templates into our format. This will be publicly released in the coming weeks.

* https://csrc.nist.gov/projects/security-content-automation-protocol/specifications/xccdf
* https://csrc.nist.gov/projects/security-content-automation-protocol/specifications/common-configuration-enumeration-cce
* https://pages.nist.gov/OSCAL/resources/
