const core = require('@actions/core');
const github = require('@actions/github');
const request = require('request');

try {

    //set header
    const headers = {
        'Accept': 'application/vnd.github.inertia-preview+json'
    };

    request('https://api.github.com/repos/guillaumefe/backlog-opencovid19/projects', headers: headers, { json: true }, (err, res, body) => {

        if (err) { return console.log(err); }
        const bodyValues = JSON.parse(body);
        console.log(body.url);
        console.log(body.explanation);
        res.send(bodyValues);

    });

} catch (error) {
  core.setFailed(error.message);
}
