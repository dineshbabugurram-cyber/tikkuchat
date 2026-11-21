// Cloudflare Pages Function. Env vars: RESEND_API_KEY, TURNSTILE_SECRET, TO_EMAIL, FROM_EMAIL
const esc=s=>String(s||'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const J=(o,s=200)=>new Response(JSON.stringify(o),{status:s,headers:{'Content-Type':'application/json'}});
export async function onRequestPost({request,env}){
let d;try{d=await request.json()}catch{return J({error:'Invalid request'},400)}
if(d.website)return J({ok:true});
if(!d.name||!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(d.email||'')||!d.message||d.consent!=='yes')return J({error:'Please complete all required fields and give consent.'},400);
if(String(d.message).length>5000)return J({error:'Message too long.'},400);
if(env.TURNSTILE_SECRET){const t=d['cf-turnstile-response'];const v=await(await fetch('https://challenges.cloudflare.com/turnstile/v0/siteverify',{method:'POST',body:new URLSearchParams({secret:env.TURNSTILE_SECRET,response:t||'',remoteip:request.headers.get('CF-Connecting-IP')||''})})).json();if(!v.success)return J({error:'Spam check failed. Please retry.'},400)}
const html=`<h3>${esc(d.type)}</h3><p><b>${esc(d.name)}</b> (${esc(d.email)})<br>${esc(d.company)}, ${esc(d.country)}<br>Interest: ${esc(d.service)}; Model: ${esc(d.model)}</p><p>${esc(d.message).replace(/\n/g,'<br>')}</p>`;
const send=(to,subject,h,reply)=>fetch('https://api.resend.com/emails',{method:'POST',headers:{Authorization:'Bearer '+env.RESEND_API_KEY,'Content-Type':'application/json'},body:JSON.stringify({from:env.FROM_EMAIL,to:[to],subject,html:h,reply_to:reply})});
const r=await send(env.TO_EMAIL,'[Website] '+d.type+': '+d.name,html,d.email);
if(!r.ok)return J({error:'Could not send. Please email us directly.'},502);
await send(d.email,'We received your enquiry','<p>Thank you for contacting TIKKUCHAT. We will reply shortly.</p>',env.TO_EMAIL);
return J({ok:true})}
