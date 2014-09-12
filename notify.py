#!/usr/bin/python
import sys
import os

SENDMAIL = "/usr/sbin/sendmail"
p = os.popen("%s -t" % SENDMAIL, "w")
p.write("To: rmohan@sonicwall.com\n")
p.write("Subject: Program exited\n")
p.write("\n") # blank line separating headers from body
for line in sys.stdin:
    p.write(line)
    print line
sts = p.close()
if sts != 0:
    print "Sendmail exit status", sts



