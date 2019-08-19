var appRouter = function(app) {
  app.get("/", function(req, res) {
      res.send("Welcome to AlphaSights SuperDay!");
  });
}

module.exports = appRouter;
