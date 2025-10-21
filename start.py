import sys

if len(sys.argv) != 3 or sys.argv[1] != '-f' or (sys.argv[2] != 'ui' and sys.argv[2] != 'non-ui'):
    print("Usage: python start.py -f <ui/non-ui>")
    sys.exit(1)

if sys.argv[2] == 'ui':
    import ui
    ui.ui()
elif sys.argv[2] == 'non-ui':
    import non_ui
    non_ui.non_ui()

# All major features completed on 17/10/2025
# Copyright © 2025 Chen Wenyuan(Raistey) All Rights Reserved
# This service only provides users with data processing and is not responsible for the user's behavior.
# Therefore, users should bear their own risks and are responsible for the content they store.