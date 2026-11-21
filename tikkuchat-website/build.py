import os,shutil,math
R='tikkuchat-website';P=R+'/public'
shutil.rmtree(R,ignore_errors=True)
for d in ['services','industries','awareness','insights','legal']:os.makedirs(f'{P}/{d}')
os.makedirs(R+'/functions/api')
DOM='https://tikkuchat.com';MAIL='info@tikkuchat.com'
S=[('soc','Security Operations (SOC)','Continuous monitoring, triage and escalation of security alerts.',['Alert triage and escalation workflows','Use-case and runbook development','Reporting aligned to agreed scope'],'Operating model, runbooks, reporting templates'),
('siem','SIEM Implementation','Design and deploy a SIEM that your team can actually operate.',['Log source onboarding and parsing','Detection rules and dashboards','Retention and cost planning'],'Architecture, onboarded sources, detection pack, handover'),
('sentinel','Microsoft Sentinel','Cloud-native SIEM and SOAR built on Microsoft Sentinel.',['Workspace design and data connectors','Analytics rules, workbooks and playbooks','Cost and ingestion optimisation'],'Deployed workspace, analytics rules, automation playbooks'),
('defender-xdr','Defender XDR','Unify endpoint, identity, email and cloud signals in Microsoft Defender XDR.',['Deployment and policy baseline','Alert tuning and incident workflows','Integration with Sentinel'],'Configured tenant, tuning report, response procedures'),
('threat-detection','Threat Detection','Detection engineering mapped to realistic attacker behaviour.',['Detection gap assessment','Rule development and testing','MITRE ATT&CK mapping'],'Coverage map, tested detections, tuning backlog'),
('incident-response','Incident Response','Preparation, handling and review of security incidents.',['IR plan and playbook design','Tabletop exercises','Investigation support and post-incident review'],'IR plan, playbooks, exercise report'),
('vulnerability-management','Vulnerability Management','A repeatable process for finding, prioritising and fixing weaknesses.',['Scanner deployment and scoping','Risk-based prioritisation','Remediation tracking'],'Process, prioritised findings, remediation dashboard'),
('cloud-security','Cloud Security','Secure configuration and monitoring for Azure, AWS and Google Cloud.',['Posture and configuration review','Identity and access hardening','Cloud logging and detection'],'Assessment report, hardening roadmap'),
('consulting','Cybersecurity Consulting','Advisory for security architecture, strategy and roadmaps.',['Security assessments','Architecture and tooling review','Roadmap and policy guidance'],'Assessment report, architecture, prioritised roadmap')]
I=[('Banking & finance','Account takeover, fraud, third-party risk, strict regulatory scrutiny.','SIEM, SOC, Incident response'),
('Healthcare','Sensitive patient data, legacy systems, ransomware exposure.','Vulnerability management, Threat detection'),
('Manufacturing','Connected operational technology, supply chain, downtime impact.','Cloud security, Consulting'),
('Education','Open networks, phishing against staff and students, limited budgets.','Defender XDR, Awareness'),
('IT & technology','Cloud sprawl, privileged access, software supply chain.','Sentinel, Cloud security, Detection'),
('Retail','Payment data, e-commerce attacks, seasonal peaks.','SIEM, Vulnerability management'),
('Government','Data sovereignty, critical services, long-lived systems.','SOC, Incident response, Consulting'),
('SMEs','Small teams, limited tooling, high exposure to phishing.','Defender XDR, Managed monitoring, Consulting')]
A=[('Phishing','Fraudulent messages that trick people into sharing credentials or running malware.',['Check the sender address, not the display name','Never approve unexpected MFA prompts','Report suspicious mail instead of deleting it']),
('Ransomware','Malware that encrypts data and demands payment.',['Keep offline, tested backups','Patch internet-facing systems quickly','Limit admin rights']),
('Malware','Software built to steal, spy or disrupt.',['Install software only from trusted sources','Keep endpoint protection active','Remove unused applications']),
('Data protection','Keeping personal and business data confidential and available.',['Collect only the data you need','Encrypt devices and backups','Review who has access regularly']),
('Security awareness','Helping every employee make safer decisions.',['Short, regular training beats annual sessions','Run phishing simulations with consent','Make reporting easy and blame-free'])]
N=[('Services','/services/'),('Industries','/industries/'),('Awareness','/awareness/'),('Insights','/insights/'),('About','/about/')]
CSS='''
:root{--n9:#070d20;--n8:#0a1128;--n7:#0f1b3d;--b:#2f6bff;--c:#00a3ff;--ink:#0b1430;--mut:#55627f;--ln:#dde3f0;--bg:#f6f8fd}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;font:17px/1.65 "IBM Plex Sans",system-ui,sans-serif;color:var(--ink);background:#fff}
h1,h2,h3{font-family:Sora,system-ui,sans-serif;line-height:1.12;letter-spacing:-.02em;margin:0 0 .5em}h1{font-size:clamp(2.4rem,6vw,4.4rem)}h2{font-size:clamp(1.7rem,3.4vw,2.5rem)}h3{font-size:1.2rem}
a{color:var(--b)}.w{max-width:1160px;margin:auto;padding:0 24px}.sec{padding:84px 0}.alt{background:var(--bg)}p{max-width:68ch}
header{position:sticky;top:0;z-index:9;background:rgba(7,13,32,.92);backdrop-filter:blur(10px);color:#fff}
.nav{display:flex;align-items:center;justify-content:space-between;height:68px}.logo{font:700 1.1rem Sora;color:#fff;text-decoration:none;letter-spacing:.06em}.logo span{color:var(--c)}
nav a{color:#c9d3ee;text-decoration:none;margin-left:26px;font-size:.95rem}nav a:hover,nav a[aria-current]{color:#fff}
.btn{display:inline-block;background:var(--b);color:#fff!important;padding:13px 24px;border-radius:6px;text-decoration:none;font-weight:600;border:0;cursor:pointer;font-size:1rem;margin-left:0}.btn:hover{background:#1f58e6}.btn.o{background:transparent;border:1px solid #4a5b8a}nav .btn{margin-left:26px;padding:9px 18px}
.m{display:none;background:0;border:1px solid #4a5b8a;color:#fff;padding:6px 12px;border-radius:6px}
.hero{background:radial-gradient(ellipse at 75% 40%,#13296b 0,var(--n8) 55%,var(--n9));color:#fff;padding:96px 0 88px;overflow:hidden}.hero .w{display:grid;grid-template-columns:1.15fr .85fr;gap:40px;align-items:center}.hero p{color:#b9c5e6;font-size:1.15rem}.hero .tag{color:var(--c);font-weight:600;margin-bottom:18px}
.sub{padding:64px 0 56px}.sub .w{display:block}
.mandala{width:100%;max-width:460px;margin:auto}.mandala .r1{transform-origin:200px 200px;animation:sp 70s linear infinite}.mandala .r2{transform-origin:200px 200px;animation:sp 110s linear infinite reverse}@keyframes sp{to{transform:rotate(360deg)}}
.g{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:20px}.card{border:1px solid var(--ln);border-radius:10px;padding:26px;background:#fff;text-decoration:none;color:var(--ink);display:block;transition:border-color .2s}a.card:hover{border-color:var(--b)}.card p{color:var(--mut);margin:0}
.two{display:grid;grid-template-columns:1fr 1fr;gap:32px}.box{border-left:3px solid var(--b);padding:4px 0 4px 22px}
.dark{background:var(--n7);color:#fff}.dark p{color:#b9c5e6}
.steps{display:flex;gap:0;flex-wrap:wrap;border:1px solid #2a3a6b;border-radius:10px;overflow:hidden}.steps button{flex:1;min-width:130px;padding:18px;background:0;border:0;color:#b9c5e6;font:600 1rem Sora;cursor:pointer;border-right:1px solid #2a3a6b}.steps button[aria-selected=true]{background:var(--b);color:#fff}
.tabs{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:22px}.tabs button{padding:10px 18px;border:1px solid var(--ln);background:#fff;border-radius:999px;cursor:pointer;font:inherit}.tabs button[aria-selected=true]{background:var(--ink);color:#fff;border-color:var(--ink)}
.panel{display:none}.panel.on{display:block}ul.t{padding-left:20px}ul.t li{margin:6px 0}
form label{display:block;font-weight:600;margin:14px 0 4px;font-size:.95rem}input,select,textarea{width:100%;padding:12px;border:1px solid #b8c2db;border-radius:6px;font:inherit}input:focus,select:focus,textarea:focus,button:focus-visible,a:focus-visible{outline:3px solid var(--c);outline-offset:2px}
.fg{display:grid;grid-template-columns:1fr 1fr;gap:0 18px}.hp{position:absolute;left:-9999px}#msg{margin-top:14px;font-weight:600}.note{background:#fff8e6;border:1px dashed #d9a400;padding:14px 18px;border-radius:8px;color:#5a4500}
footer{background:var(--n9);color:#9fb0da;padding:56px 0 28px;font-size:.95rem}footer a{color:#c9d3ee;text-decoration:none;display:block;margin:6px 0}footer .g{grid-template-columns:2fr 1fr 1fr 1fr}footer h4{color:#fff;margin:0 0 10px;font-family:Sora}
@media(max-width:860px){.hero .w,.two,.fg,footer .g{grid-template-columns:1fr}.mandala{max-width:300px}.m{display:block}nav{display:none;position:absolute;top:68px;left:0;right:0;background:var(--n9);padding:12px 24px 24px}nav.open{display:block}nav a{display:block;margin:12px 0}nav .btn{display:inline-block;margin:8px 0 0}}
@media(prefers-reduced-motion:reduce){.mandala *{animation:none!important}html{scroll-behavior:auto}}
'''
JS='''
document.querySelector('.m').onclick=function(){document.querySelector('nav').classList.toggle('open')};
document.querySelectorAll('[role=tablist]').forEach(function(l){var b=l.querySelectorAll('[role=tab]');b.forEach(function(t){t.onclick=function(){b.forEach(function(x){x.setAttribute('aria-selected',x==t);var p=document.getElementById(x.dataset.p);if(p)p.classList.toggle('on',x==t)});var f=document.getElementById('ft');if(f&&t.dataset.type)f.value=t.dataset.type}})});
var f=document.getElementById('cf');if(f)f.onsubmit=async function(e){e.preventDefault();var m=document.getElementById('msg');m.textContent='Sending…';try{var r=await fetch('/api/contact',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(Object.fromEntries(new FormData(f)))});var j=await r.json();m.textContent=r.ok?'Thank you. We have received your enquiry and will reply by email.':(j.error||'Something went wrong. Email us directly.');if(r.ok)f.reset()}catch(x){m.textContent='Network error. Please email us directly.'}};
'''
def mandala():
    s='<svg class="mandala" viewBox="0 0 400 400" role="img" aria-label="Geometric shield mandala"><defs><linearGradient id="g" x1="0" x2="1" y1="0" y2="1"><stop stop-color="#2f6bff"/><stop offset="1" stop-color="#00a3ff"/></linearGradient></defs>'
    s+='<g class="r2" fill="none" stroke="#2f6bff" stroke-opacity=".5"><circle cx="200" cy="200" r="190" stroke-dasharray="2 8"/>'
    for i in range(24):
        a=i*math.pi/12;s+=f'<circle cx="{200+190*math.cos(a):.1f}" cy="{200+190*math.sin(a):.1f}" r="3" fill="#00a3ff" stroke="none"/>'
    s+='</g><g class="r1" fill="none" stroke="#00a3ff" stroke-opacity=".6">'
    for i in range(12):
        a=i*30;s+=f'<ellipse cx="200" cy="105" rx="26" ry="62" transform="rotate({a} 200 200)"/>'
    s+='</g><circle cx="200" cy="200" r="86" fill="#0a1128" stroke="url(#g)" stroke-width="2"/><path d="M200 140l42 16v34c0 28-18 48-42 58-24-10-42-30-42-58v-34z" fill="none" stroke="url(#g)" stroke-width="3"/><path d="M200 170v50M178 195h44" stroke="#fff" stroke-width="3" stroke-linecap="round"/></svg>'
    return s
def page(path,title,desc,body,hero=None):
    nv=''.join(f'<a href="{u}"'+(' aria-current="page"' if path.startswith(u) and u!='/' else '')+f'>{n}</a>' for n,u in N)
    robots='<meta name="robots" content="noindex">' if os.environ.get('STAGING') else ''
    url=DOM+path
    ld='{"@context":"https://schema.org","@type":"Organization","name":"TIKKUCHAT","url":"'+DOM+'","email":"'+MAIL+'","slogan":"Ancient Wisdom. Modern Cyber Defence."}'
    h=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title><meta name="description" content="{desc}"><link rel="canonical" href="{url}">{robots}<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:type" content="website"><meta property="og:url" content="{url}"><meta name="theme-color" content="#0a1128"><link rel="icon" href="/favicon.svg"><link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;600&family=Sora:wght@600;700&display=swap" rel="stylesheet"><link rel="stylesheet" href="/style.css"><script type="application/ld+json">{ld}</script></head><body>
<header><div class="w nav"><a class="logo" href="/">TIKKU<span>CHAT</span></a><button class="m" aria-label="Menu">Menu</button><nav>{nv}<a class="btn" href="/contact/">Request a consultation</a></nav></div></header><main>{body}</main>
<footer><div class="w"><div class="g"><div><h4>TIKKUCHAT</h4><p>Ancient Wisdom. Modern Cyber Defence.</p><p><a href="mailto:{MAIL}">{MAIL}</a></p></div><div><h4>Services</h4>{''.join(f'<a href="/services/{s[0]}/">{s[1]}</a>' for s in S[:5])}</div><div><h4>Company</h4><a href="/about/">About</a><a href="/industries/">Industries</a><a href="/awareness/">Awareness Centre</a><a href="/insights/">Insights</a><a href="/contact/">Contact</a></div><div><h4>Legal</h4><a href="/legal/privacy/">Privacy policy</a><a href="/legal/cookies/">Cookie policy</a><a href="/legal/terms/">Terms</a></div></div><p style="margin-top:36px">© 2026 TIKKUCHAT. All rights reserved.</p></div></footer><script src="/app.js"></script></body></html>'''
    fp=P+path+('index.html' if path.endswith('/') else '')
    os.makedirs(os.path.dirname(fp),exist_ok=True);open(fp,'w').write(h)
def sub(t,p):return f'<section class="hero sub"><div class="w"><h1>{t}</h1><p>{p}</p></div></section>'
cta='<section class="sec dark"><div class="w"><h2>Talk to us about your security goals</h2><p>Tell us about your environment and we will suggest a practical starting point.</p><a class="btn" href="/contact/">Request a consultation</a></div></section>'
sv=''.join(f'<a class="card" href="/services/{s[0]}/"><h3>{s[1]}</h3><p>{s[2]}</p></a>' for s in S)
journey=['Assess','Design','Implement','Monitor','Improve']
jt={'Assess':'We review your assets, logs, risks and existing controls to find the gaps that matter most.','Design':'We define architecture, detection priorities and ownership that fit your size and budget.','Implement':'We deploy and integrate tooling, onboard data sources and build detections and playbooks.','Monitor':'Where agreed, we monitor and triage alerts, or equip your team to do it.','Improve':'We tune detections, review incidents and update the roadmap as threats and systems change.'}
jb=''.join(f'<button role="tab" data-p="j{i}" aria-selected="{str(i==0).lower()}">{j}</button>' for i,j in enumerate(journey))
jp=''.join(f'<div id="j{i}" class="panel{" on" if i==0 else ""}" style="padding:26px 4px"><p>{jt[j]}</p></div>' for i,j in enumerate(journey))
page('/','TIKKUCHAT | Global Cybersecurity Services and Consulting','TIKKUCHAT delivers SOC, SIEM, Microsoft Sentinel, Defender XDR, incident response and cybersecurity consulting for organisations worldwide.',f'''
<section class="hero"><div class="w"><div><p class="tag">Ancient Wisdom. Modern Cyber Defence.</p><h1>Protection, engineered for modern threats.</h1><p>We help organisations detect threats earlier, respond with confidence and build security that lasts, through projects and ongoing services.</p><p><a class="btn" href="/contact/">Request a consultation</a> &nbsp; <a class="btn o" href="/services/">Explore services</a></p></div>{mandala()}</div></section>
<section class="sec"><div class="w"><h2>What we do</h2><p>Detection, response and secure design across your environment.</p><div class="g">{sv}</div></div></section>
<section class="sec alt"><div class="w"><h2>Two ways to work with us</h2><div class="two"><div class="box"><h3>Project-based</h3><p>SIEM implementation, security assessments, architecture, integrations and defined security projects with clear scope and deliverables.</p></div><div class="box"><h3>Recurring services</h3><p>Managed security services, SIEM maintenance, monitoring and ongoing advisory. Service levels and hours are defined in each agreement.</p></div></div></div></section>
<section class="sec dark"><div class="w"><h2>Our security journey</h2><div class="steps" role="tablist">{jb}</div>{jp}</div></section>
<section class="sec"><div class="w"><h2>Industries we support</h2><p>Security priorities differ by sector. We start from yours.</p><div class="g">{''.join(f'<a class="card" href="/industries/"><h3>{i[0]}</h3></a>' for i in I)}</div></div></section>
<section class="sec alt"><div class="w"><h2>The Tikkuchat platform: planned</h2><p>We intend to grow into Tikkuchat SOC, Tikkuchat Cloud, Tikkuchat Intelligence, Tikkuchat Consulting, Tikkuchat Academy and Tikkuchat Labs. These are future plans and not yet available.</p></div></section>{cta}''')
page('/about/','About TIKKUCHAT','Our vision, mission and approach to practical cybersecurity.',sub('About TIKKUCHAT','Protection, defence and safeguarding, delivered with practical expertise.')+f'''<section class="sec"><div class="w two"><div class="box"><h2>Vision</h2><p>To become a trusted global cybersecurity brand, combining professional services, technology and, in time, our own security products.</p></div><div class="box"><h2>Mission</h2><p>To help organisations of every size understand their risk and build security they can run and trust.</p></div></div></section><section class="sec alt"><div class="w"><h2>How we work</h2><div class="g"><div class="card"><h3>Practical first</h3><p>We prioritise controls that reduce real risk.</p></div><div class="card"><h3>Transparent</h3><p>Clear scope, honest capabilities and plain reporting.</p></div><div class="card"><h3>Built to last</h3><p>We document and hand over so your team can own the outcome.</p></div></div></div></section>{cta}''')
page('/services/','Cybersecurity Services | TIKKUCHAT','SOC, SIEM, Microsoft Sentinel, Defender XDR, threat detection, incident response, vulnerability management, cloud security and consulting.',sub('Cybersecurity services','Delivered as projects, recurring services or a combination.')+f'<section class="sec"><div class="w"><div class="g">{sv}</div></div></section>{cta}')
for s in S:
    page(f'/services/{s[0]}/',f'{s[1]} | TIKKUCHAT',s[2],sub(s[1],s[2])+f'''<section class="sec"><div class="w two"><div><h2>What we do</h2><ul class="t">{''.join(f'<li>{x}</li>' for x in s[3])}</ul></div><div><h2>Typical deliverables</h2><p>{s[4]}.</p><h3>Engagement</h3><p>Available as a fixed-scope project or, where agreed, an ongoing service.</p></div></div></section>{cta}''')
tb=''.join(f'<button role="tab" data-p="i{k}" aria-selected="{str(k==0).lower()}">{i[0]}</button>' for k,i in enumerate(I))
pn=''.join(f'<div id="i{k}" class="panel{" on" if k==0 else ""}"><div class="card"><h3>{i[0]}</h3><p><b>Typical risks:</b> {i[1]}</p><p><b>Relevant services:</b> {i[2]}</p><p>Regulatory requirements vary by country. We help map controls to your obligations but do not provide legal advice or compliance guarantees.</p></div></div>' for k,i in enumerate(I))
page('/industries/','Industry Solutions | TIKKUCHAT','Cybersecurity for banking, healthcare, manufacturing, education, IT, retail, government and SMEs.',sub('Industry solutions','Select your sector.')+f'<section class="sec"><div class="w"><div class="tabs" role="tablist">{tb}</div>{pn}</div></section>{cta}')
ac=''.join(f'<div class="card"><h3>{a[0]}</h3><p>{a[1]}</p><ul class="t">{"".join(f"<li>{x}</li>" for x in a[2])}</ul></div>' for a in A)
page('/awareness/','Cyber Awareness Centre | TIKKUCHAT','Plain-language guidance on phishing, ransomware, malware, data protection and security awareness.',sub('Cyber Awareness Centre','Clear, practical guidance for people and teams.')+f'<section class="sec"><div class="w"><div class="g">{ac}</div></div></section><section class="sec alt"><div class="w"><p>Full articles and guides will be published here. See <a href="/insights/">Insights</a>.</p></div></section>')
page('/insights/','Resources & Insights | TIKKUCHAT','Technical blogs, research, implementation guides, case studies and cybersecurity updates.',sub('Resources & Insights','Technical blogs, guides, research and case studies.')+'<section class="sec"><div class="w"><div class="g"><div class="card"><h3>Technical blog</h3><p>No posts published yet.</p></div><div class="card"><h3>Implementation guides</h3><p>No guides published yet.</p></div><div class="card"><h3>Case studies</h3><p>Published only when a client engagement can be shared with permission.</p></div></div></div></section>')
fm=f'''<section class="sec"><div class="w"><div class="tabs" role="tablist"><button role="tab" aria-selected="true" data-type="Consultation request">Consultation</button><button role="tab" aria-selected="false" data-type="Project enquiry">Project enquiry</button><button role="tab" aria-selected="false" data-type="Partnership enquiry">Partnership</button></div>
<form id="cf" style="max-width:760px"><input type="hidden" name="type" id="ft" value="Consultation request"><div class="fg"><div><label for="n">Full name</label><input id="n" name="name" required></div><div><label for="e">Work email</label><input id="e" name="email" type="email" required></div><div><label for="c">Company</label><input id="c" name="company" required></div><div><label for="k">Country</label><input id="k" name="country"></div></div>
<label for="s">Area of interest</label><select id="s" name="service"><option>Not sure yet</option>{''.join(f'<option>{s[1]}</option>' for s in S)}</select><label for="m">Engagement model</label><select id="m" name="model"><option>Project-based</option><option>Recurring service</option><option>Not sure</option></select>
<label for="t">How can we help?</label><textarea id="t" name="message" rows="5" required></textarea><input class="hp" name="website" tabindex="-1" autocomplete="off" aria-hidden="true">
<label style="font-weight:400"><input type="checkbox" name="consent" value="yes" required style="width:auto"> I agree that TIKKUCHAT may use these details to respond to my enquiry, as described in the <a href="/legal/privacy/">privacy policy</a>.</label>
<div class="cf-turnstile" data-sitekey="TURNSTILE_SITE_KEY"></div><p><button class="btn" type="submit">Send enquiry</button></p><div id="msg" role="status"></div></form><p>Or email <a href="mailto:{MAIL}">{MAIL}</a>.</p></div></section><script src="https://challenges.cloudflare.com/turnstile/v0/api.js" async defer></script>'''
page('/contact/','Contact TIKKUCHAT','Request a consultation, discuss a project or enquire about a partnership.',sub('Contact us','Consultations, project discussions and partnership requests.')+fm)
def legal(slug,t,body):page(f'/legal/{slug}/',f'{t} | TIKKUCHAT',t,sub(t,'Draft template. Have it reviewed by a qualified lawyer before launch.')+f'<section class="sec"><div class="w"><div class="note">Draft for legal review. Replace bracketed items.</div>{body}</div></section>')
legal('privacy','Privacy policy','<h3>Who we are</h3><p>TIKKUCHAT, [legal entity, address]. Contact: '+MAIL+'.</p><h3>Data we collect</h3><p>Only what you submit through our forms (name, email, company, country, message) and basic analytics.</p><h3>Why and legal basis</h3><p>To respond to your enquiry (consent or legitimate interests).</p><h3>Retention</h3><p>[Retention period].</p><h3>Your rights</h3><p>Access, correction, deletion, restriction, portability and objection. Contact us to exercise them.</p><h3>Processors</h3><p>[Email provider, hosting: Cloudflare].</p>')
legal('cookies','Cookie policy','<p>This site sets no non-essential cookies. If analytics or marketing cookies are added later, we will request consent first. [Update accordingly.]</p>')
legal('terms','Terms of use','<p>Content is for general information and is not a contract or professional advice. [Add liability, IP and governing-law terms.]</p>')
page('/404.html','Page not found | TIKKUCHAT','Page not found',sub('Page not found','Return to the <a href="/" style="color:#00a3ff">home page</a>.'))
open(P+'/style.css','w').write(CSS);open(P+'/app.js','w').write(JS)
open(P+'/favicon.svg','w').write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="12" fill="#0a1128"/><path d="M32 10l18 7v14c0 12-8 20-18 24-10-4-18-12-18-24V17z" fill="none" stroke="#2f6bff" stroke-width="4"/></svg>')
open(P+'/robots.txt','w').write('User-agent: *\n'+('Disallow: /\n' if os.environ.get('STAGING') else 'Allow: /\n')+f'Sitemap: {DOM}/sitemap.xml\n')
urls=[]
for r,_,fs in os.walk(P):
    for f in fs:
        if f=='index.html':urls.append(r[len(P):]+'/')
open(P+'/sitemap.xml','w').write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{DOM}{u if u!="//" else "/"}</loc></url>' for u in sorted(urls))+'</urlset>')
open(P+'/_headers','w').write("/*\n  Strict-Transport-Security: max-age=31536000; includeSubDomains\n  X-Content-Type-Options: nosniff\n  X-Frame-Options: DENY\n  Referrer-Policy: strict-origin-when-cross-origin\n  Permissions-Policy: camera=(), microphone=(), geolocation=()\n  Content-Security-Policy: default-src 'self'; script-src 'self' https://challenges.cloudflare.com 'unsafe-inline'; style-src 'self' https://fonts.googleapis.com 'unsafe-inline'; font-src https://fonts.gstatic.com; frame-src https://challenges.cloudflare.com; connect-src 'self'; img-src 'self' data:\n")
open(R+'/functions/api/contact.js','w').write('''// Cloudflare Pages Function. Env vars: RESEND_API_KEY, TURNSTILE_SECRET, TO_EMAIL, FROM_EMAIL
const esc=s=>String(s||'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const J=(o,s=200)=>new Response(JSON.stringify(o),{status:s,headers:{'Content-Type':'application/json'}});
export async function onRequestPost({request,env}){
let d;try{d=await request.json()}catch{return J({error:'Invalid request'},400)}
if(d.website)return J({ok:true});
if(!d.name||!/^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$/.test(d.email||'')||!d.message||d.consent!=='yes')return J({error:'Please complete all required fields and give consent.'},400);
if(String(d.message).length>5000)return J({error:'Message too long.'},400);
if(env.TURNSTILE_SECRET){const t=d['cf-turnstile-response'];const v=await(await fetch('https://challenges.cloudflare.com/turnstile/v0/siteverify',{method:'POST',body:new URLSearchParams({secret:env.TURNSTILE_SECRET,response:t||'',remoteip:request.headers.get('CF-Connecting-IP')||''})})).json();if(!v.success)return J({error:'Spam check failed. Please retry.'},400)}
const html=`<h3>${esc(d.type)}</h3><p><b>${esc(d.name)}</b> (${esc(d.email)})<br>${esc(d.company)}, ${esc(d.country)}<br>Interest: ${esc(d.service)}; Model: ${esc(d.model)}</p><p>${esc(d.message).replace(/\\n/g,'<br>')}</p>`;
const send=(to,subject,h,reply)=>fetch('https://api.resend.com/emails',{method:'POST',headers:{Authorization:'Bearer '+env.RESEND_API_KEY,'Content-Type':'application/json'},body:JSON.stringify({from:env.FROM_EMAIL,to:[to],subject,html:h,reply_to:reply})});
const r=await send(env.TO_EMAIL,'[Website] '+d.type+': '+d.name,html,d.email);
if(!r.ok)return J({error:'Could not send. Please email us directly.'},502);
await send(d.email,'We received your enquiry','<p>Thank you for contacting TIKKUCHAT. We will reply shortly.</p>',env.TO_EMAIL);
return J({ok:true})}
''')
open(R+'/README.md','w').write('''# TIKKUCHAT website
Static site (no build step). Output directory: `public`. Forms: `functions/api/contact.js`.
## Deploy on Cloudflare Pages
1. Push this folder to GitHub. Cloudflare > Workers & Pages > Create > Pages > connect repo.
2. Build command: (none). Output directory: `public`.
3. Settings > Variables and Secrets: RESEND_API_KEY, TURNSTILE_SECRET, TO_EMAIL, FROM_EMAIL (e.g. "TIKKUCHAT <noreply@tikkuchat.com>").
4. Replace TURNSTILE_SITE_KEY in public/contact/index.html (or in build.py) with your Turnstile site key.
5. Custom domains: add tikkuchat.com and www.
## Staging
`STAGING=1 python3 build.py` adds noindex and blocks crawlers. Rebuild without it for launch.
## Regenerate pages
Edit build.py (copy, services, industries) and run `python3 build.py`.
''')
shutil.copy('build.py',R+'/build.py')
