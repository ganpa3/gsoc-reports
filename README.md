# GSoC Reports
Get all the student reports of all the organizations of all the years (since 2016)!

# Why?
When applying for GSoC, it's quite helpful to know how the organization works. How the experience of the past students was. You can also get links to student proposals which you can take inspiration from to write your own proposal.

Note: Running this script for all years will take a long time. You have been warned!

This script will run 5 times (2016 - 2020)

Around 200 organizations participate in GSoC every year. That will be (200 * 5 =) **1000 requests for organizations**.

Each year, around 1200 projects are accepted. So, that will be (1200 * 5 =) **6000 requests for students**.

So, in total, around (5 + 1000 + 6000 =) **7005 requests will be made**!

That's huge.

I didn't have the patience for that. I ran the script for last 3 years (2018 - 2020) and uploaded the data in [data.json](https://github.com/ganpa3/gsoc-reports/blob/main/data.json).

You can, e.g., use [jq](https://stedolan.github.io/jq/) to easily get the reports for your desired organization.

Note: Organization names can vary each year. Use the name given on the GSoC website to get the reports.

Be careful with quoting issues in your shell. If the organization name contains spaces or unicode characters, use double quotes.

For example, to get all the student reports for Zulip
```bash
$ jq '."Zulip"' data.json
{
  "2020": {
    "org_url": "https://summerofcode.withgoogle.com/archive/2020/organizations/5924162381545472/",
    "number_of_students": 18,
    "reports": {
      "Clara Moraes Dantas": "https://docs.google.com/document/d/1Jr0eDyhLQ5oA0ShC0DEMjy2n7s4DFIr8PtS-jbDpqyc/edit?usp=sharing",
      "Preet Mishra": "https://gist.github.com/preetmishra/8bca59e92d4a3890bb07638e62ee0b55",
      "MANAV MEHTA": "https://gist.github.com/manavmehta/4acf7bf3720f6e87bf24ec5295c1cb84",
      "Mohit Gupta-1": "https://gist.github.com/thedeveloperr/0e75649034e103efe7549d96ca09f9e3",
      "Kartik Srivastava": "https://gist.github.com/akashaviator/ac5c003498b16084dd2d2f21badf896a",
      "Hashir Sarwar": "https://hashirsarwar.github.io/gsoc2020/",
      "Sahil Batra": "https://gist.github.com/sahil839/754c7a92add0b5bd5bf25d42306bdee3",
      "Aditya Verma-1": "https://www.dropbox.com/scl/fi/akk7cwazhfdl7tz8zwc7n/GSoC-20-with-Zulip.paper?dl=0&rlkey=5hys0paowmqyalxumzikh63ue",
      "Jagan Sivam": "https://gist.github.com/Jagansivam28/a11836e0ba24971f25903fe51d755693",
      "Kaustubh Nair": "https://gist.github.com/kaustubh-nair/5c2aa05d1e89ad8171d7fa35ff723a42",
      "Priyank": "https://gist.github.com/priyank-p/65526e59c45d4d2b968dede4238db9b8",
      "Siddharth Varshney": "https://gist.github.com/SiddharthVarshney/9c572e9aab9a9175331953657b56d333",
      "Arpit Sharma": "https://gist.github.com/arpit551/d875fc6b6f6bb3ef56645abc160d8b95",
      "Ryan Rehman": "https://gist.github.com/ryanreh99/270a7a15e7980d2409562c5a7a085349",
      "Vinit Singh": "https://gist.github.com/vinitS101/4ae30f0425f3bcb579eed547293609af",
      "agrawal-d": "https://gist.github.com/agrawal-d/cf01504a3e763e872a7b3e93499494dc",
      "Dinesh Chidipothu": "https://gist.github.com/chdinesh1089/39d38cf17601cedd3d5467023411b09a",
      "Tejas Tank": "https://gist.github.com/majordwarf/6ffdb3a0ef89c14aac2294a6c2f7cd7b"
    }
  },
  "2018": {
    "org_url": "https://summerofcode.withgoogle.com/archive/2018/organizations/4721112676040704/",
    "number_of_students": 10,
    "reports": {
      "Yashashvi Dave": "https://gist.github.com/YJDave/df46f970f27b3e051ec64efc31e5b6fb",
      "Yago González": "https://paper.dropbox.com/doc/Zulip-GSoC-18-Progress-Log--AKHprLQSudfxichvRAUFP75YAQ-fToU3JiPwOyrPHJuhAHWr",
      "Eeshan Garg": "https://paper.dropbox.com/doc/Eeshan-Garg-GSoC-Work-Product-2018--AKEY36tLDsiMwcc3qGKs5HFVAQ-osHpL9uT7u18vNktWBZZX",
      "Aswin G": "https://medium.com/@agzuniverse/gsoc-work-product-submission-683c65ef3c82",
      "Shubham Dhama": "https://gist.github.com/shubhamdhama/5057e5e008e7172f93b72efbcfa34bef",
      "Shubham Padia": "https://gist.github.com/shubham-padia/3b1309194354a63aa96072f7764a5181",
      "Aditya Bansal": "https://paper.dropbox.com/doc/Google-Summer-Of-Code-2018-Project-Report--AKF4_YfQ~m9X6FwbfHbM~AshAQ-F7kUfwRW4hiS8TSiLpEZC",
      "Rhea Parekh": "https://gist.github.com/rheaparekh/6ffd73cf2a2dcd816a6a5058c18edc06",
      "Abhigyan Khaund": "https://gist.github.com/abhigyank/decf6160ab574631375a9b00e6f4b6a8",
      "Aman Agrawal": "https://github.com/zulip/zulip-terminal/"
    }
  }
}
```

```bash
$ jq '."Zulip Open Source Project"' data.json
{
  "2019": {
    "org_url": "https://summerofcode.withgoogle.com/archive/2019/organizations/4652389204754432/",
    "number_of_students": 17,
    "reports": {
      "PRAGATI AGRAWAL": "https://gist.github.com/pragatiagrawal31/6e72eb8e37b3c18c5b5e0c9d1d5a0f67",
      "Yashashvi Dave": "https://gist.github.com/YJDave/4e59f250cf7027dd80eca10a272e07c3",
      "Wyatt Hoodes": "https://whoodes.github.io/project-gsoc-zulip/",
      "Thomas Ip": "https://gist.github.com/tommyip/2799ada1c8c3c2951d9b1d25ca6c44ab",
      "Hemanth V. Alluri": "https://gist.github.com/Hypro999/720c8ee92e7d53d662306e84af09a784",
      "Yash Rathore": "https://gist.github.com/YashRE42/5ec42c7390e30fee3e0a029804e9c7b9",
      "Vipul Sharma-1": "https://gist.github.com/vsvipul/a22818db200c98910f2b1bc1cdf5179f",
      "Mohit-thedeveloperr": "https://gist.github.com/thedeveloperr/4c2630545b4c052deb45a7d86077e75c",
      "Sumanth V Rao": "https://gist.github.com/sumanthvrao/696c0ea86e7c1abf58394db626803008",
      "Mateusz Mandera": "https://gist.github.com/mateuszmandera/e5c7b285ada7a5a2254e4e899d1fc0fd",
      "Vinit Singh": "https://gist.github.com/vinitS101/b6bbecdf6d4bf1e8e14f2e5ff0a3980d",
      "Kanishk Kakar": "https://kanishk98.github.io/2019/08/21/gsoc-with-zulip/",
      "Vaibhav .": "https://gist.github.com/vrongmeal/f5cd3bbfa75f1abd5bfb870e3190f029",
      "Isham Mahajan": "https://ishammahajan.github.io/misc/gsoc-evaluations/",
      "Aman Agrawal": "https://gist.github.com/amanagr/4fc8cd0070479c661b569806a2dba01b",
      "Alexandra Ciobica": "https://gist.github.com/alexandraciobica/9e32216993417fd8cd583bc4b0350dbf",
      "Rohitt Vashishtha": "https://gist.github.com/aero31aero/3b6b469688b56741d060737eb455e12e"
    }
  }
}
```
