// Load the AWS SDK for Node.js
// const AWS = require('aws-sdk');
import AWS from 'aws-sdk';

// Set the region
AWS.config.update({region: 'REGION'});

// Create EC2 service object
const ec2 = new AWS.EC2({apiVersion: '2016-11-15'});

const params = {
    InstanceIds: ['INSTANCE_ID'],
    DryRun: true
};

if (process.argv[2].toUpperCase() === "ON") {
    // Call EC2 to start monitoring the selected instances
    ec2.monitorInstances(params, function (err, data) {
        if (err && err.code === 'DryRunOperation') {
            params.DryRun = false;
            ec2.monitorInstances(params, function (err, data) {
                if (err) {
                    console.log("Error", err);
                } else if (data) {
                    console.log("Success", data.InstanceMonitorings);
                }
            });
        } else {
            console.log("You don't have permission to change instance monitoring.");
        }
    });
} else if (process.argv[2].toUpperCase() === "OFF") {
    // Call EC2 to stop monitoring the selected instances
    ec2.unmonitorInstances(params, function (err, data) {
        if (err && err.code === 'DryRunOperation') {
            params.DryRun = false;
            ec2.unmonitorInstances(params, function (err, data) {
                if (err) {
                    console.log("Error", err);
                } else if (data) {
                    console.log("Success", data.InstanceMonitorings);
                }
            });
        } else {
            console.log("You don't have permission to change instance monitoring.");
        }
    });
}
