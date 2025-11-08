import smtplib

try:
    email = input('Enter Sender Email: ')
    receiver_email = input('Enter Receiver Email: ')
    subject = input('SUBJECT: ')
    message = input('MESSAGE: ')

    text = f"Subject: {subject}\n\n{message}"

    # Try connecting to the SMTP server
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587, timeout=10)
        server.starttls()
    except Exception as e:
        print(" Failed to connect to SMTP server.")
        print("Error:", e)
        raise SystemExit()

    # Try logging in
    try:
        server.login(email, "vcvbgskynhcbvlyf")  # Use an App Password, not your real Gmail password
    except smtplib.SMTPAuthenticationError:
        print(" Authentication failed. Check your email or app password.")
        server.quit()
        raise SystemExit()
    except Exception as e:
        print(" Error during login.")
        print("Error:", e)
        server.quit()
        raise SystemExit()

    # Try sending the email
    try:
        server.sendmail(email, receiver_email, text)
        print(f" Email has been sent successfully to {receiver_email}")
    except smtplib.SMTPRecipientsRefused:
        print("The receiver email address is invalid.")
    except Exception as e:
        print("Failed to send the email.")
        print("Error:", e)
    finally:
        server.quit()

except KeyboardInterrupt:
    print("\n Process interrupted by user.")
except Exception as e:
    print(" An unexpected error occurred.")
    print("Error:", e)
