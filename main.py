import struct
import wave

import streamlit as st
from pyarrow import null
import pandas as pd
import time
import streamlit as st
import plotly.express as px
import random
import requests
import re

import os
import requests

import requests
import asyncio
from shazamio import Shazam

from pvrecorder import PvRecorder
from audiorecorder import audiorecorder

st.title("Audio Recorder")
audiobytes = audiorecorder("Click to record", "Click to stop recording")

if audiobytes:
    st.audio(audiobytes, format="audio/wavs")
