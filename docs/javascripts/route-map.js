/*
 * Route map for the Harness Engineering Guide landing pages.
 *
 * Each landing page carries:
 *   - <div id="route-map">: where the map is drawn;
 *   - <script type="application/json" id="route-map-data">: copy for one language;
 *   - <div class="route-map-fallback">: the same routes in Markdown, with links
 *     tagged data-route / data-node. The map reads every href from those links,
 *     so the strict MkDocs build validates them. Without JavaScript, or with
 *     broken data, the fallback simply stays visible.
 *
 * Geometry is shared by both languages and lives here; copy lives in the page.
 * No dependencies.
 */
(function () {
  "use strict";

  var SVG_NS = "http://www.w3.org/2000/svg";

  var LAYOUT = {
    width: 640,
    height: 430,
    box: { w: 170, h: 56 },
    nodes: {
      guide: [235, 10],
      template: [40, 110],
      brain: [430, 110],
      work: [235, 210],
      observatory: [40, 310],
      lab: [430, 310]
    },
    edges: [
      "M270,66 L165,108",
      "M370,66 L475,108",
      "M165,166 L270,208",
      "M475,166 L370,208",
      "M270,266 L165,308",
      "M370,266 L475,308",
      "M212,338 L426,338"
    ],
    learn: [
      "M515,366 L515,408 L18,408 L18,138 L36,138",
      "M602,338 L622,338 L622,38 L408,38"
    ],
    labels: [
      ["learnTemplate", 200, 424],
      ["learnGuide", 470, 24],
      ["signals", 290, 330]
    ]
  };

  function readData() {
    var block = document.getElementById("route-map-data");
    if (!block) return null;
    try {
      var data = JSON.parse(block.textContent);
      if (!data || !data.ui || !data.nodes || !Array.isArray(data.routes)) return null;
      for (var id in LAYOUT.nodes) {
        if (!data.nodes[id]) return null;
      }
      for (var i = 0; i < data.routes.length; i++) {
        var steps = data.routes[i].steps;
        if (!Array.isArray(steps)) return null;
        for (var j = 0; j < steps.length; j++) {
          if (!LAYOUT.nodes[steps[j].node]) return null;
        }
      }
      return data.routes.length ? data : null;
    } catch (err) {
      return null;
    }
  }

  function hrefFor(kind, id) {
    var link = document.querySelector(
      ".route-map-fallback a[data-" + kind + '="' + id + '"]'
    );
    return link ? link.getAttribute("href") : null;
  }

  function html(tag, className, text) {
    var el = document.createElement(tag);
    if (className) el.className = className;
    if (text !== undefined) el.textContent = text;
    return el;
  }

  function svg(tag, attrs, text) {
    var el = document.createElementNS(SVG_NS, tag);
    for (var key in attrs) el.setAttribute(key, attrs[key]);
    if (text !== undefined) el.textContent = text;
    return el;
  }

  function link(className, text, href) {
    var a = html("a", className, text);
    a.setAttribute("href", href);
    return a;
  }

  var view = null;

  function buildMap(root, data) {
    var ui = data.ui;
    var routesBar = html("div", "rm-routes");
    routesBar.setAttribute("role", "group");
    routesBar.setAttribute("aria-label", ui.question);

    var buttons = {};
    data.routes.forEach(function (route) {
      var button = html("button", "rm-route");
      button.type = "button";
      button.setAttribute("aria-pressed", "false");
      button.appendChild(html("span", "rm-route__label", route.label));
      button.appendChild(html("span", "rm-route__who", route.audience));
      button.addEventListener("click", function () {
        render({ route: route.id, node: null });
      });
      buttons[route.id] = button;
      routesBar.appendChild(button);
    });

    var map = svg("svg", {
      class: "rm-svg",
      viewBox: "0 0 " + LAYOUT.width + " " + LAYOUT.height,
      role: "group",
      "aria-label": ui.mapLabel
    });
    var defs = svg("defs", {});
    var marker = svg("marker", {
      id: "rm-arrow",
      viewBox: "0 0 10 10",
      refX: "9",
      refY: "5",
      markerWidth: "7",
      markerHeight: "7",
      orient: "auto-start-reverse"
    });
    marker.appendChild(svg("path", { d: "M0,0 L10,5 L0,10 z", class: "rm-arrowhead" }));
    defs.appendChild(marker);
    map.appendChild(defs);

    LAYOUT.edges.forEach(function (d) {
      map.appendChild(svg("path", { d: d, class: "rm-edge", "marker-end": "url(#rm-arrow)" }));
    });
    LAYOUT.learn.forEach(function (d) {
      map.appendChild(
        svg("path", { d: d, class: "rm-edge rm-edge--learn", "marker-end": "url(#rm-arrow)" })
      );
    });
    LAYOUT.labels.forEach(function (label) {
      map.appendChild(svg("text", { x: label[1], y: label[2], class: "rm-edge-label" }, ui[label[0]]));
    });

    var nodes = {};
    Object.keys(LAYOUT.nodes).forEach(function (id) {
      var pos = LAYOUT.nodes[id];
      var copy = data.nodes[id];
      var x = pos[0];
      var y = pos[1];
      var cx = x + LAYOUT.box.w / 2;
      var group = svg("g", {
        class: "rm-node",
        "data-node": id,
        tabindex: "0",
        role: "button",
        "aria-label": copy.label + ": " + copy.sub
      });
      group.appendChild(
        svg("rect", { x: x, y: y, width: LAYOUT.box.w, height: LAYOUT.box.h, rx: 12, class: "rm-box" })
      );
      group.appendChild(svg("text", { x: cx, y: y + 25, class: "rm-label", "text-anchor": "middle" }, copy.label));
      group.appendChild(svg("text", { x: cx, y: y + 43, class: "rm-sub", "text-anchor": "middle" }, copy.sub));
      var badge = svg("g", { class: "rm-badge", "aria-hidden": "true" });
      badge.appendChild(svg("circle", { cx: x + 4, cy: y + 4, r: 12 }));
      var badgeText = svg("text", { x: x + 4, y: y + 8, "text-anchor": "middle" }, "");
      badge.appendChild(badgeText);
      group.appendChild(badge);

      function select() {
        render({ route: view.state.route, node: id });
      }
      group.addEventListener("click", select);
      group.addEventListener("keydown", function (event) {
        if (event.key === "Enter" || event.key === " " || event.key === "Spacebar") {
          event.preventDefault();
          select();
        }
      });
      nodes[id] = { group: group, badgeText: badgeText };
      map.appendChild(group);
    });

    var panel = html("div", "rm-panel");
    panel.setAttribute("aria-live", "polite");

    var layout = html("div", "rm-layout");
    var mapWrap = html("div", "rm-map");
    mapWrap.appendChild(map);
    layout.appendChild(mapWrap);
    layout.appendChild(panel);

    root.appendChild(routesBar);
    root.appendChild(layout);

    view = {
      data: data,
      buttons: buttons,
      nodes: nodes,
      panel: panel,
      state: { route: data.routes[0].id, node: null }
    };
  }

  function routeById(id) {
    var routes = view.data.routes;
    for (var i = 0; i < routes.length; i++) {
      if (routes[i].id === id) return routes[i];
    }
    return routes[0];
  }

  function render(state) {
    if (!view) return;
    view.state = state;
    var data = view.data;
    var ui = data.ui;
    var route = routeById(state.route);

    Object.keys(view.buttons).forEach(function (id) {
      var on = id === route.id;
      view.buttons[id].setAttribute("aria-pressed", on ? "true" : "false");
      view.buttons[id].classList.toggle("is-on", on);
    });

    var order = {};
    route.steps.forEach(function (step, index) {
      if (!(step.node in order)) order[step.node] = index + 1;
    });
    Object.keys(view.nodes).forEach(function (id) {
      var node = view.nodes[id];
      var lit = id in order;
      node.group.classList.toggle("is-lit", lit);
      node.group.classList.toggle("is-dim", !lit);
      node.group.classList.toggle("is-selected", id === state.node);
      node.badgeText.textContent = lit ? String(order[id]) : "";
    });

    var panel = view.panel;
    panel.textContent = "";
    panel.appendChild(html("h3", "rm-panel__title", route.label));
    panel.appendChild(html("p", "rm-panel__who", ui.routeFor + ": " + route.audience));

    var list = html("ol", "rm-steps");
    route.steps.forEach(function (step, index) {
      var item = html("li", "rm-step");
      item.appendChild(html("span", "rm-step__n", String(index + 1)));
      var body = html("div", "rm-step__body");
      body.appendChild(html("strong", "rm-step__text", step.text));
      body.appendChild(html("span", "rm-step__node", data.nodes[step.node].label));
      if (step.tags && step.tags.length) {
        var tags = html("span", "rm-step__tags");
        step.tags.forEach(function (tag) {
          tags.appendChild(html("span", "hk-tag" + (tag.easy ? " is-easy" : ""), tag.text));
        });
        body.appendChild(tags);
      }
      item.appendChild(body);
      list.appendChild(item);
    });
    panel.appendChild(list);

    var routeHref = hrefFor("route", route.id);
    if (routeHref) panel.appendChild(link("rm-open", ui.openRoute + " →", routeHref));

    var detail = html("div", "rm-detail");
    if (state.node) {
      var copy = data.nodes[state.node];
      detail.appendChild(html("h4", "rm-detail__title", copy.label));
      var facts = html("dl", "rm-detail__facts");
      [["what", copy.what], ["who", copy.who]].forEach(function (pair) {
        facts.appendChild(html("dt", "", ui[pair[0]]));
        facts.appendChild(html("dd", "", pair[1]));
      });
      facts.appendChild(html("dt", "", ui.first));
      var firstDd = html("dd", "");
      var nodeHref = hrefFor("node", state.node);
      if (nodeHref) {
        firstDd.appendChild(link("", copy.first, nodeHref));
      } else {
        firstDd.textContent = copy.first;
      }
      facts.appendChild(firstDd);
      detail.appendChild(facts);
    } else {
      detail.appendChild(html("p", "rm-detail__hint", ui.tapHint));
    }
    panel.appendChild(detail);
  }

  function init() {
    var root = document.getElementById("route-map");
    if (!root || root.getAttribute("data-ready") === "true") return;
    var data = readData();
    if (!data) return;
    buildMap(root, data);
    render(view.state);
    root.setAttribute("data-ready", "true");
    if (root.parentNode) root.parentNode.classList.add("route-map-ready");
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
