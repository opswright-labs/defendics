# DefendICS (pronounced defendix)

This project is a collection of tools, scripts and data catalogs and other useful information focused on security hardening in critical infrastructure. 

Our belief is that this is a critical, but missing, capability for security misconfiguration efficacy and prioritization.

The initial release includes the only known implementation of a CCSS (Common Configuration Scoring System) tool that is the implementation of the [proposed CCSS approach by NIST](https://www.nist.gov/publications/common-configuration-scoring-system-ccss-metrics-software-security-configuration). While we don't believe that this is any better than CVSS, it's one of the only quantifiable methods documented today. And this precisely is what we will be working on in future releases of defendics.

For information on how we are approaching this topic, check out the articles on security hardening at [opswright.com](https://www.opswright.com/topic/security-hardening).

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
