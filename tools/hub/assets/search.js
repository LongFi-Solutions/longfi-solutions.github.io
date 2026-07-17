(function () {
  var input = document.getElementById("search-input"), box = document.getElementById("search-results");
  if (!input || !box) return;
  var docs = null, items = [], active = -1;
  function load(){ return docs ? Promise.resolve(docs)
    : fetch("/assets/hub/search-index.json").then(function(r){return r.json();}).then(function(j){docs=j;return j;}); }
  function esc(s){return String(s).replace(/[&<>"]/g,function(c){return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c];});}
  function snippet(text, terms){
    var lc=text.toLowerCase(), pos=-1;
    terms.forEach(function(t){var p=lc.indexOf(t); if(p>=0&&(pos<0||p<pos))pos=p;});
    if(pos<0)pos=0;
    var start=Math.max(0,pos-45), end=Math.min(text.length,pos+130);
    var frag=(start>0?"…":"")+text.slice(start,end)+(end<text.length?"…":"");
    frag=esc(frag);
    terms.forEach(function(t){ if(!t)return; var re=new RegExp("("+t.replace(/[.*+?^${}()|[\]\\]/g,"\\$&")+")","ig"); frag=frag.replace(re,"<mark>$1</mark>"); });
    return frag;
  }
  function score(d, terms){
    var s=0, t=(d.title||"").toLowerCase(), h=(d.headings||"").toLowerCase(), b=(d.text||"").toLowerCase();
    terms.forEach(function(term){ if(!term)return;
      if(t.indexOf(term)>=0)s+=10; if(h.indexOf(term)>=0)s+=4; if(b.indexOf(term)>=0)s+=1; });
    return s;
  }
  function render(q){
    var terms=q.toLowerCase().split(/\s+/).filter(Boolean);
    if(!terms.length){close();return;}
    var res=docs.map(function(d){return {d:d,s:score(d,terms)};}).filter(function(x){return x.s>0;});
    res.sort(function(a,b){return b.s-a.s;}); res=res.slice(0,8);
    if(!res.length){box.innerHTML='<div class="sr-empty">No results for “'+esc(q)+'”</div>';box.classList.add("open");items=[];return;}
    box.innerHTML=res.map(function(x){return '<a class="sr-item" href="'+esc(x.d.url)+'">'
      +'<div class="sr-crumb">'+esc(x.d.section||"")+'</div>'
      +'<div class="sr-title">'+esc(x.d.title)+'</div>'
      +'<div class="sr-snip">'+snippet(x.d.text||"",terms)+'</div></a>';}).join("");
    box.classList.add("open"); items=[].slice.call(box.querySelectorAll(".sr-item")); active=-1;
  }
  function close(){box.classList.remove("open");box.innerHTML="";items=[];active=-1;}
  function upd(){items.forEach(function(el,i){el.classList.toggle("active",i===active);}); if(items[active])items[active].scrollIntoView({block:"nearest"});}
  function go(){var q=input.value.trim(); if(!q){close();return;} load().then(function(){render(q);}); }
  input.addEventListener("input", go);
  input.addEventListener("focus", function(){ if(input.value.trim()) go(); });
  input.addEventListener("keydown", function(e){
    if(!box.classList.contains("open"))return;
    if(e.key==="ArrowDown"){e.preventDefault();active=Math.min(items.length-1,active+1);upd();}
    else if(e.key==="ArrowUp"){e.preventDefault();active=Math.max(0,active-1);upd();}
    else if(e.key==="Enter"&&active>=0&&items[active]){e.preventDefault();location.href=items[active].getAttribute("href");}
    else if(e.key==="Escape"){close();input.blur();}
  });
  document.addEventListener("click", function(e){ if(!e.target.closest(".search")) close(); });
})();
