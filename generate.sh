#!/bin/bash

protoc -I=tfplugin --python_out=tfplugin tfplugin/tfplugin5.proto
