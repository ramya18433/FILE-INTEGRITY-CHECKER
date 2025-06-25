# FILE-INTEGRITY-CHECKER

*company : CODETECH IT SOLUTION

*NAME* : Meesala Ramya

*INTERN ID * : CT04DF610

*DOMAIN * :CYBER SECURITY AND ETHICAL HACKING 

*DURATION*  : 4 WEEKS 

*MENTER*  : NEELA SANTOSH

##DELIVERABLE: A PYTHON SCRIPT
USING LIBRARIES LIKE HASHLIB TO
ENSURE FILE INTEGRITY.

File Integrity Verification Using Python and Hashlib
In today’s digital environment, maintaining the integrity of files is crucial to ensuring data security and reliability. File integrity means ensuring that a file remains unchanged, unaltered, and free from unauthorized modifications. One of the most effective ways to verify file integrity is by using cryptographic hash functions. In this project, I developed a Python script using the hashlib library to perform file integrity checks. The script calculates and compares hash values to detect any changes in the file's content.

I used Visual Studio Code (VS Code) as the development environment for this task. VS Code offers a lightweight, user-friendly interface with robust features that make Python development efficient and straightforward. By utilizing VS Code, I was able to write, test, and execute the Python script seamlessly.

The core of this project is the hashlib library, which is a built-in Python module providing access to many secure hash algorithms, such as MD5, SHA-1, SHA-256, and more. Hash functions generate a fixed-size string, called a hash or digest, from the contents of a file. Even a minor change in the file will result in a completely different hash value, making this technique highly effective for file integrity verification.

The Python script I created works by first reading the contents of a given file in binary mode. It then processes the content using a hash function (in this case, SHA-256, which is widely used for its balance of speed and security). The script calculates the current hash value of the file and compares it with a previously stored hash. If the two hashes match, the file is considered intact; if they differ, it indicates that the file has been altered, either intentionally or due to corruption.

The process I followed involved creating a .py file in VS Code, writing the code using Python's hashlib and os libraries, and testing the script with different files. I opened the VS Code terminal and executed the script using the python filename.py command. This approach allowed me to easily track outputs, debug issues, and ensure the script performed accurately.

This method of verifying file integrity is practical for various applications, including software distribution, system administration, and cybersecurity. It helps ensure that files remain unaltered during transfer, storage, or use. For example, developers often provide checksum values alongside software downloads so that users can verify the authenticity and integrity of the files they receive.

In conclusion, using Python's hashlib library provides a simple yet powerful way to ensure file integrity. With the help of VS Code, I successfully developed, tested, and ran a Python script capable of detecting unauthorized changes to files by comparing hash values. This project highlights the importance of file integrity in maintaining secure and reliable systems.

##

![Image](https://github.com/user-attachments/assets/011bd450-0321-42a3-aa44-47748472c81d)




