import time
import customtkinter as ctk
import sys
import os
import winrt.windows.graphics.imaging as imaging
import winrt.windows.storage.streams as streams
import winrt.windows.foundation
from PIL import Image

class Misc:
    def resource_path(self, relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller/Nuitka """
        if getattr(sys, 'frozen', False):
            # If frozen (PyInstaller, Nuitka, cx_Freeze)
            if hasattr(sys, '_MEIPASS'):
                # PyInstaller
                base_path = sys._MEIPASS
            else:
                # Nuitka, cx_Freeze - use __file__ as it points to extraction dir
                # This file is in autoappraiser/utils, so the package root is one level up
                base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        else:
            # Development: use the directory of the package
            base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            
        full_path = os.path.join(base_path, relative_path)
        
        # Fallback to CWD if not found, for backward compatibility
        if not os.path.exists(full_path):
            cwd_path = os.path.join(os.path.abspath("."), relative_path)
            if os.path.exists(cwd_path):
                return cwd_path
            
            # Additional fallback for Nuitka if structure is flattened
            exe_dir_path = os.path.join(os.path.dirname(sys.executable), relative_path)
            if os.path.exists(exe_dir_path):
                return exe_dir_path
                
        return full_path
