#! /bin/bash
./dockerbuild.sh
# Replace with your Google Cloud project id
gcloud docker -- push gcr.io/PROJECT_ID/api-server
