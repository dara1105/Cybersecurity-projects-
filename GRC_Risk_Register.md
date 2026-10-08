# GRC Portfolio: Enterprise Cybersecurity Risk Register

## 📌 Project Overview
This project demonstrates the application of Governance, Risk, and Compliance (GRC) principles by establishing a foundational **Cybersecurity Risk Register** for a hypothetical enterprise. It utilizes standard risk management methodologies (aligned with **NIST SP 800-30**) to identify vulnerabilities, calculate risk scores, and propose strategic security mitigations.

## 📊 Risk Assessment Matrix (Likelihood x Impact = Risk Rating)
* Scale used: 1 (Low) to 5 (High)
* Risk Rating: Low (1-5), Medium (6-12), High (15-25)

| Risk ID | Asset / Vulnerability | Threat Source | Likelihood (1-5) | Impact (1-5) | Risk Score (L x I) | Proposed Mitigation Strategy (Controls) |
| :--- | :--- | :--- | :---: | :---: | :---: | :--- |
| **RSK-01** | Employee Credentials / Phishing Attacks | External Threat Actors | 5 | 4 | **20 (HIGH)** | Implement Mandatory Multi-Factor Authentication (MFA) and conduct bi-monthly phishing simulation training. |
| **RSK-02** | Customer Databases / Unpatched Software | Ransomware Groups | 3 | 5 | **15 (HIGH)** | Establish an automated patch management policy and enforce daily, encrypted off-site backups. |
| **RSK-03** | Corporate Laptops / Device Theft | Physical Loss / Malicious Insider | 2 | 3 | **6 (MEDIUM)** | Enforce Full Disk Encryption (BitLocker) and deploy Mobile Device Management (MDM) for remote wiping capability. |
| **RSK-04** | Cloud Servers / Misconfigured S3 Buckets | Human Error / Administrators | 3 | 4 | **12 (MEDIUM)** | Implement Continuous Cloud Security Posture Management (CSPM) and enforce the Principle of Least Privilege (PoLP) via IAM roles. |

## 🛡️ Frameworks & Standards Referenced
* **NIST SP 800-30:** Guide for Conducting Risk Assessments.
* **ISO/IEC 27001 (Control A.12.6):** Technical Vulnerability Management.
* **SOC 2 (Trust Services Criteria):** Security and Confidentiality baselines.

## 🧠 Skills Demonstrated
* Qualitative Risk Analysis & Risk Calculation
* Security Policy Formulation & Control Mapping
* Regulatory Compliance Alignment (NIST/ISO)
