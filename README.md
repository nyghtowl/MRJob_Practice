## MRJob Practice


To run the code locally, use the following in the CLI:
    python <path/filename for code> <path/file to process> > <output filename>


Note the ">" that does not have a match above is actual bash script to say to pass the results into the file that is created.

*****

#### Running AWS

Check out this link to find out how to setup AWS to run the [script](https://pythonhosted.org/mrjob/guides/emr-quickstart.html).

Setup a [config file](https://pythonhosted.org/mrjob/guides/configs-basics.html) to cut down on the number of parameters in the command line to run MRJob on AWS.

Example config file:

    runners:
      emr:
        cmdenv:
          TZ: America/Los_Angeles
        aws_access_key_id: <key>
        aws_secret_access_key: <key>
        ec2_key_pair: EMR
        ec2_key_pair_file: ~/.ssh/EMR.pem
        ssh_tunnel_to_job_tracker: true

To run the job on AWS use the following code:
    python <path/code to run job> -r emr <path data to process> --output-dir=s3://my_bucket/wc-out/ --no-output

Note
* output is where the data is stored
* no output prevents data from being stored locally (good if the data is large)
