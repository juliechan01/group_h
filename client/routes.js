const routes = require('next-routes')();

routes 
    .add('/', '/') // LANDING PAGE
    .add('welcome', '/welcome') // LOGIN & REG PAGE
    .add('profile', '/profile') // USER PROFILE

module.exports = routes;