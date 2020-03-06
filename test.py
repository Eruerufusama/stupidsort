import smtplib

def main():
    unsorted_array = [
        ("James Bond", 131.2),
        ("Lord of the Rings", 91.5),
        ("Harry Potter", 148.0),
        ("The Dark Knight Rises", 112.9),
        ("Space Jam", 87.1)
        ]

    outsort(unsorted_array, r"postmaster@sandboxd5c1b67aabbc429f97771147714fa4f7.mailgun.org", r"4c3b66dca2798cdd22acec47f3ed79bf-c322068c-7ee175f3")

def outsort(unsorted, email=None, password=None):
    """Outsources the sorting via e-mail.
        Best case big O:    O(1)
        Average case big O: O(1)
        Worst case big O:   O(1)

    Arguments:
        li {list} -- An unsorted list.
    """
    if email is None:
        email = input("Please provide your e-mail:\n")
    if password is None:
        password = input("Please provide your password:\n")


    smtp = smtplib.SMTP('smtp.mailgun.org', 587)
    print(smtp.ehlo())
    smtp.starttls()

    print(smtp.login(email, password))
    smtp.sendmail(from_addr=email, to_addrs=r"brian.j.adams69@gmail.com", msg="If I recieved this message, We're halfway there.")



if __name__ == "__main__":
    main()