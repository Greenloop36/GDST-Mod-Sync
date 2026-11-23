# Source - https://stackoverflow.com/a/65084936
# Posted by Novel, modified by community. See post 'Timeline' for change history
# Retrieved 2026-11-23, License - CC BY-SA 4.0

from tkinter import *
from tkinter import ttk
import threading
import time

def generate_reports(start, end):
    print("provide a mcve next time!")
    time.sleep(5)

def run_report(root, *args):
    generate_reports(*args)
    root.event_generate("<<PhishDoneEvent>>") # yes, this is using tkinter in a thread, but some tkinter methods are ok to use in threads

class BillingApp:
  def __init__(self, root):
    self.mainframe = ttk.Frame(root, padding = '4 4 12 12')
    self.mainframe.grid(column = 0, row = 0, sticky = (N, W, E, S))
    ttk.Button(self.mainframe, text = "Generate Billing Reports", command = self.do_reports).grid(column = 2, row = 3, sticky = (W, E))
    root.bind("<<PhishDoneEvent>>", self.report_done)

  def do_reports(self, *args):
    # note this makes a new widget with every click ... this is bad. Refactor to reuse the widget. 
    self.pbar = ttk.Progressbar(self.mainframe, orient = HORIZONTAL, mode = 'indeterminate')
    self.pbar.grid(row = 4, column = 3, sticky = (W, E))
    start, end = 4,5
    t1 = threading.Thread(target = run_report, args = [root, start, end])
    t1.start()
    self.pbar.start()

  def report_done(self, event=None):
    self.pbar.stop()
    Label(self.mainframe, text="report done").grid(row = 4, column = 3)

root = Tk()
BillingApp(root)
root.mainloop()
