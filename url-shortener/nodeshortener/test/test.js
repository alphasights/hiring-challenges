var assert = require('assert');
var http = require('http');

describe('The Basic shortner', function() {
  describe('home page', function() {
    it('should return 200', function() {
      http.get('http://localhost:3000/', (resp) => {
        assert.equal(resp.statusCode, 200);
      });
    });
  });
});
