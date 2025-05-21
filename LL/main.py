from package import DLL, ReverseDll

# dll = DLL()
# dll.display_forward()
# dll.display_backward()
rdll = ReverseDll()
rdll.append(11)
rdll.append(22)
rdll.append(33)
rdll.append(44)
rdll.display_forward()
rdll.reverse()
rdll.display_forward()