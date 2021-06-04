const kue = require('kue');
const queue = kue.createQueue();

const jobData = {
  phoneNumber: '4153518780',
  message: 'This is the code to verify your account',
}

const job = queue.create('push_notification_code', jobData).save(function(err) {
  if (!err) {
    console.log(`Notification job created: ${job.id}`);
  } else console.log('Notification job failed');
});

job.on('complete', function(res) {
  console.log('Notification job completed');
});

job.on('failed', function() {
  console.log('Notification job failed');
});
