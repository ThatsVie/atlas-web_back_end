# NoSQL


## Resources

- [NoSQL Databases Explained](https://riak.com/resources/nosql-databases/)
- [What is NoSQL ? (YouTube)](https://www.youtube.com/watch?v=qUV2j3XBRHc)
- [MongoDB with Python Crash Course](https://www.youtube.com/watch?v=E-1xI85Zog8)
- [MongoDB Tutorial 2: Insert, Update, Remove, Query](https://www.youtube.com/watch?v=CB9G5Dvv-EE)
- [Aggregation in MongoDB](https://www.mongodb.com/docs/manual/aggregation/)
- [Introduction to MongoDB and Python](https://realpython.com/introduction-to-mongodb-and-python/)
- [mongo Shell Methods](https://www.mongodb.com/docs/manual/reference/method/)
- [The mongo Shell](https://www.mongodb.com/docs/mongodb-shell/)



## Learning Objectives


- What NoSQL means (hint: it's not "not SQL").
- Differences between SQL and NoSQL (the relational chaos vs. the document freedom).
- What ACID is and why NoSQL databases sometimes play it fast and loose with those rules.
- What document storage is and why you won’t need 10 different JOINs to find that one piece of data.
- Types of NoSQL databases.
- Benefits of NoSQL databases in a world that increasingly feels like it's spiraling out of control.
- How to query, insert, update, and delete data in MongoDB like a responsible adult who doesn't accidentally drop entire databases.
- How to use MongoDB effectively, even if you’re still wondering whether SQL will ever forgive you.


## Requirements

 <details>
<summary> <strong>MongoDB Command Files</strong></summary>

- Files must be interpreted/compiled on Ubuntu 20.04 LTS using MongoDB (version 4.4).
- Each file should end with a new line (yes, really).
- The first line of every file must be a comment (`// my comment`).
- A `README.md` file, like this one, is mandatory (you’ve come to the right place!).
- The length of files will be tested using `wc`.
</details>

<details>
<summary> <strong>Python Scripts</strong></summary>

- Files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.9 and PyMongo 4.8.0.
- Each file should end with a new line.
- The first line must be `#!/usr/bin/env python3` (so the interpreter knows what’s up).
- Follow `pycodestyle` (version 2.5.*) like a sacred text.
- All functions and modules must be documented.
- Make sure your code doesn’t execute when imported (that’s what `if __name__ == "__main__":` is for).
  </details>

## Step-by-Step Walkthrough: Installing MongoDB 4.4 on Ubuntu 20.04 (What Worked for Me)
<details>
<summary> <strong>This is the detailed process that worked for me while installing MongoDB 4.4 on Ubuntu 20.04, especially resolving issues related to `libssl1.1` dependencies. If you're following along, keep in mind that your system setup may differ, and minor adjustments could be necessary.</strong></summary>

### 1. Install Prerequisites
MongoDB requires `gnupg` and `curl` to manage keys and repositories. Run the following commands to ensure these are installed:

```bash
sudo apt-get install gnupg curl
```

### 2. Import MongoDB Public GPG Key
To verify the MongoDB packages, I imported the public GPG key using the command below:

```bash
curl -fsSL https://www.mongodb.org/static/pgp/server-4.4.asc | sudo gpg -o /usr/share/keyrings/mongodb-server-4.4.gpg --dearmor
```

### 3. Create the MongoDB Source List
Next, I created a MongoDB source list to add the repository for Ubuntu 20.04:

```bash
echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-4.4.gpg ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list
```

### 4. Reload Local Package Database
I refreshed the package manager to recognize the newly added MongoDB repository:

```bash
sudo apt-get update
```

### 5. Install `libssl1.1`
MongoDB 4.4 depends on `libssl1.1`, which is no longer in the default repositories. Here's how I manually installed `libssl1.1`:

```bash
wget http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.1f-1ubuntu2_amd64.deb
sudo dpkg -i libssl1.1_1.1.1f-1ubuntu2_amd64.deb
```

### 6. Install MongoDB
Once `libssl1.1` was installed, I proceeded to install MongoDB:

```bash
sudo apt-get install -y mongodb-org
```

### 7. Start MongoDB
After installation, I started MongoDB by running:

```bash
sudo systemctl start mongod
```

### 8. Enable MongoDB to Start on Boot
To ensure MongoDB starts automatically after a reboot, I enabled it with:

```bash
sudo systemctl enable mongod
```

### 9. Verify MongoDB Installation
Finally, I verified that MongoDB was working by running the MongoDB shell:

```bash
mongo
```

This opened the MongoDB shell, confirming the installation was successful.
</details>


## Tasks and Usage
