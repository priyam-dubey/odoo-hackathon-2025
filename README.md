Skill Swap Platform – Odoo Hackathon 2025 Submission

 **Problem Statement**
Develop a Skill Swap Platform — a mini application that enables users to list their skills and
request others in return


### 🔑 Features:
- User Profile with:
  - Name, Location, Profile Photo
  - Skills Offered
  - Skills Wanted
  - Availability (weekends/evenings)
- Skill Swap Requests:
  - Accept / Reject / Delete Requests
  - View Pending & Accepted Swaps
  - Leave Ratings/Feedback
- Admin Features:
  - Reject inappropriate skills
  - Ban users violating rules
  - Platform-wide messaging
  - Export reports and stats

---

## 👨‍💻 Team Members

| Name                | Role              | Email                        |
|---------------------|-------------------|-------------------------------|
| Priyambad Kumar Dubey | Developer & Lead  | priyambaddubey2004@gmail.com  |
| Satyarth Singh        | Backend Developer | satyarth8292218622@gmail.com  |

---

## 🎥 Demo Video

#todo later

> 📌 Replace `VIDEO_ID_HERE` with your uploaded YouTube video ID.

---

## 📁 Module Structure
skill_swap_platform/
├── init.py
├── manifest.py
├── models/
│ ├── init.py
│ ├── user_profile.py
│ ├── skill.py
│ └── swap_request.py
├── views/
│ ├── user_profile_views.xml
│ ├── skill_views.xml
│ └── swap_request_views.xml
└── security/
└── ir.model.access.csv


## 🛠 Tech Stack

- Python
- Odoo 16.0
- XML (for views & forms)
- PostgreSQL (Odoo default DB)
- GitHub for collaboration

This module is structured for Odoo 16.0. To install:
- Place `skill_swap_platform` inside your Odoo `addons/` folder.
- Restart the Odoo server and update the apps list.

