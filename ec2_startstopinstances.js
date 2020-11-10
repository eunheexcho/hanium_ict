// Load the AWS SDK for Node.js
// const AWS = require('aws-sdk');
import AWS from 'aws-sdk';

// Set the region
AWS.config.update({region: 'REGION'});

// Create EC2 service object
const ec2 = new AWS.EC2({apiVersion: '2016-11-15'});

const params = {
    InstanceIds: [process.argv[3]],
    DryRun: true
};

if (process.argv[2].toUpperCase() === "START") {
    // Call EC2 to start the selected instances
    ec2.startInstances(params, function (err, data) {
        if (err && err.code === 'DryRunOperation') {
            params.DryRun = false;
            ec2.startInstances(params, function (err, data) {
                if (err) {
                    console.log("Error", err);
                } else if (data) {
                    console.log("Success", data.StartingInstances);
                }
            });
        } else {
            console.log("You don't have permission to start instances.");
        }
    });
} else if (process.argv[2].toUpperCase() === "STOP") {
    // Call EC2 to stop the selected instances
    ec2.stopInstances(params, function (err, data) {
        if (err && err.code === 'DryRunOperation') {
            params.DryRun = false;
            ec2.stopInstances(params, function (err, data) {
                if (err) {
                    console.log("Error", err);
                } else if (data) {
                    console.log("Success", data.StoppingInstances);
                }
            });
        } else {
            console.log("You don't have permission to stop instances");
        }
    });
}
