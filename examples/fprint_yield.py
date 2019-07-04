from fprint import *

init()
ddevs = DiscoveredDevices()
dev = ddevs[0].open_device()

# r = FP_ENROLL_RETRY
# while r != FP_ENROLL_COMPLETE:
    # r, pd = dev.enrol_finger()
    # if r < 0:
        # raise RuntimeError("Internal I/O error while enrolling: %i" % r)
    # if r == FP_ENROLL_COMPLETE:
        # print("enroll complete")
    # if r == FP_ENROLL_FAIL:
        # print("Failed. Enrollment process reset.")
        # break
    # if r == FP_ENROLL_PASS:
        # print("enroll PASS")
        # pass
    # if r == FP_ENROLL_RETRY:
        # print("enroll RETRY")
        # pass
    # if r == FP_ENROLL_RETRY_TOO_SHORT:
        # print("enroll RETRY_SHORT")
        # pass
    # if r == FP_ENROLL_RETRY_CENTER_FINGER:
        # print("enroll RETRY_CENTER")
        # pass
    # if r == FP_ENROLL_RETRY_REMOVE_FINGER:
        # print("enroll RETRY_REMOVE")

while True:
    r = next(dev.enroll_finger_loop_async())
    if r == FP_ENROLL_COMPLETE:
        break;
    print("Doing......{0}".format(r))
print("DONE")

dev.enroll_finger_loop()
