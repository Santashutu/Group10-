# using Tkinter interface to search for .java files

import os
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox as msg


def Interface(self):
    Label(self.app, text="URL: ").grid(row=0, column=0, sticky='w', pady=2)
    Entry(self.app, textvariable=self.url, width=40).grid(row=0, column=1, sticky='w', columnspan=2, pady=2, padx=2)

    Label(self.app, text="Destination:").grid(row=2, column=0, sticky='w', pady=2)
    self.destination = Entry(self.app, textvariable=self.location, width=40)
    self.destination.grid(row=2, column=1, sticky='w', columnspan=2, pady=2, padx=2)
    self.destination.bind("<Button-1>", self.Destination)
    Button(self.app, text="Get Resolution", command=self.StreamSelection).grid(row=2, column=3, sticky='e', pady=2,
                                                                               padx=2)