#! /usr/bin/python
import smtpd
import asyncore

smtpd.DebuggingServer(("127.0.0.1", 30026), None)

asyncore.loop()
