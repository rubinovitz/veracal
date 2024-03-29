function S4() {
  return (((1 + Math.random()) * 65536) | 0).toString(16).substring(1)
}
function guid() {
  return (S4() + S4() + "-" + S4() + "-" + S4() + "-" + S4() + "-" + S4() + S4() + S4())
}
window.Store = function (b) {
  this.name = b;
  var a = localStorage.getItem(this.name);
  this.records = (a && a.split(",")) || []
};
_.extend(Store.prototype, {
  save: function () {
    localStorage.setItem(this.name, this.records.join(","))
  },
  create: function (a) {
    if (!a.id) {
      a.id = a.attributes.id = guid()
    }
    localStorage.setItem(this.name + "-" + a.id, JSON.stringify(a));
    this.records.push(a.id);
    this.save();
    return a
  },
  update: function (a) {
    localStorage.setItem(this.name + "-" + a.id, JSON.stringify(a));
    if (!_.include(this.records, a.id)) {
      this.records.push(a.id)
    }
    this.save();
    return a
  },
  find: function (a) {
    return JSON.parse(localStorage.getItem(this.name + "-" + a.id))
  },
  findAll: function () {
    return _.map(this.records, function (a) {
      return JSON.parse(localStorage.getItem(this.name + "-" + a))
    }, this)
  },
  destroy: function (a) {
    localStorage.removeItem(this.name + "-" + a.id);
    this.records = _.reject(this.records, function (b) {
      return b == a.id
    });
    this.save();
    return a
  }
});
Backbone.sync = function (f, c, e, b) {
  var d;
  var a = c.localStorage || c.collection.localStorage;
  switch (f) {
  case "read":
    d = c.id ? a.find(c) : a.findAll();
    break;
  case "create":
    d = a.create(c);
    break;
  case "update":
    d = a.update(c);
    break;
  case "delete":
    d = a.destroy(c);
    break
  }
  if (d) {
    e(d)
  } else {
    b("Record not found")
  }
};
