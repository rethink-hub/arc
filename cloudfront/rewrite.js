// CloudFront viewer-request function for arcassistant.app (deployed by
// .github/workflows/deploy.yml). REDIRECTS is filled in at deploy time from
// _data/redirects.yml by cloudfront/build-function.rb, so retiring a URL is a
// one-line edit there, not a change to this file.
var REDIRECTS = __REDIRECTS__;

function qs(req) {
  var parts = [];
  for (var k in req.querystring) {
    var v = req.querystring[k];
    if (v.multiValue) v.multiValue.forEach(function (m) { parts.push(k + "=" + m.value); });
    else parts.push(v.value === "" ? k : k + "=" + v.value);
  }
  return parts.length ? "?" + parts.join("&") : "";
}

function redirect(code, location) {
  return { statusCode: code, statusDescription: code === 301 ? "Moved Permanently" : "Found",
    headers: { location: { value: location } } };
}

function handler(event) {
  var req = event.request;
  var host = req.headers.host ? req.headers.host.value : "";
  var uri = req.uri;

  // www → apex
  if (host.indexOf("www.") === 0) return redirect(301, "https://" + host.slice(4) + uri + qs(req));

  // Retired URLs (old .html pages, github.io-era paths, merged posts)
  var to = REDIRECTS[uri] || REDIRECTS[uri.endsWith("/") ? uri.slice(0, -1) : uri + "/"];
  if (to) return redirect(301, to + qs(req));

  // Any other old .html URL → its pretty form (/x.html → /x/, /x/index.html → /x/)
  if (uri.endsWith(".html") && uri !== "/404.html") {
    return redirect(301, uri.replace(/(\/index)?\.html$/, "/").replace(/^\/+$/, "/") + qs(req));
  }

  // Pretty referral/route links → their query form (mirrors the fallback in 404.md)
  var seg = uri.split("/").filter(Boolean);
  if (seg.length === 2 && seg[0] === "r" && /^[A-Za-z0-9]{1,16}$/.test(seg[1])) {
    return redirect(302, "/r/?c=" + encodeURIComponent(seg[1].toUpperCase()));
  }
  if (seg.length === 2 && seg[0] === "s" && /^[a-z0-9._-]{1,64}$/i.test(seg[1])) {
    return redirect(302, "/s/?c=" + encodeURIComponent(seg[1].toLowerCase()));
  }
  if ((seg.length === 2 || seg.length === 3) && seg[0] === "go" && /^[a-z0-9_-]+(\/[a-z0-9_-]+)?$/i.test(seg.slice(1).join("/"))) {
    return redirect(302, "/go/?to=" + encodeURIComponent(seg.slice(1).join("/").toLowerCase()));
  }

  // /x/ → /x/index.html ; /x → /x/
  if (uri.endsWith("/")) req.uri += "index.html";
  else if (uri.lastIndexOf(".") < uri.lastIndexOf("/")) return redirect(301, uri + "/" + qs(req));
  return req;
}
