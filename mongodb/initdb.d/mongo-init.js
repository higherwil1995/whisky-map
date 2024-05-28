db.createCollection("whisky");
db.createCollection("account");
db.createUser({
    user: "wilson",
    pwd: "1234",
    roles: [
      {
        role: "root",
        db: "app",
      },
    ],
  });
