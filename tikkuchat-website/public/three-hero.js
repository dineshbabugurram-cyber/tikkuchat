import * as THREE from 'https://cdn.jsdelivr.net/npm/three@0.180.0/build/three.module.js';
const canvas=document.querySelector('#cyber-scene');
if(canvas){
 const reduced=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
 const scene=new THREE.Scene();
 const camera=new THREE.PerspectiveCamera(38,1,.1,100);camera.position.set(0,0,8);
 const renderer=new THREE.WebGLRenderer({canvas,alpha:true,antialias:true});
 renderer.setPixelRatio(Math.min(window.devicePixelRatio||1,1.8));
 const root=new THREE.Group();scene.add(root);
 const core=new THREE.Mesh(new THREE.IcosahedronGeometry(1.22,2),new THREE.MeshPhysicalMaterial({color:0x9bdcff,metalness:.38,roughness:.2,transparent:true,opacity:.82}));
 root.add(core);
 const wire=new THREE.Mesh(new THREE.IcosahedronGeometry(1.34,2),new THREE.MeshBasicMaterial({color:0x2563eb,wireframe:true,transparent:true,opacity:.34}));root.add(wire);
 const shield=new THREE.Mesh(new THREE.OctahedronGeometry(.72,1),new THREE.MeshBasicMaterial({color:0xffffff,wireframe:true,transparent:true,opacity:.7}));root.add(shield);
 const rings=[];
 [1.72,2.05,2.36].forEach((radius,index)=>{const ring=new THREE.Mesh(new THREE.TorusGeometry(radius,.009,8,150),new THREE.MeshBasicMaterial({color:index===1?0x0ea5e9:0x3b82f6,transparent:true,opacity:.55}));ring.rotation.x=Math.PI*(.28+index*.16);ring.rotation.y=Math.PI*(.18+index*.2);root.add(ring);rings.push(ring);});
 const particleGeometry=new THREE.BufferGeometry(),count=700,positions=new Float32Array(count*3);
 for(let i=0;i<count;i++){const radius=2.6+Math.random()*1.3,a=Math.random()*Math.PI*2,b=Math.acos(2*Math.random()-1);positions[i*3]=radius*Math.sin(b)*Math.cos(a);positions[i*3+1]=radius*Math.sin(b)*Math.sin(a);positions[i*3+2]=radius*Math.cos(b);}
 particleGeometry.setAttribute('position',new THREE.BufferAttribute(positions,3));
 const particles=new THREE.Points(particleGeometry,new THREE.PointsMaterial({color:0x3b82f6,size:.018,transparent:true,opacity:.7}));scene.add(particles);
 scene.add(new THREE.AmbientLight(0xffffff,2));
 const light=new THREE.PointLight(0x60a5fa,24,20);light.position.set(3,3,5);scene.add(light);
 let targetX=0,targetY=0;
 const resize=()=>{const width=canvas.clientWidth||480,height=canvas.clientHeight||420;renderer.setSize(width,height,false);camera.aspect=width/height;camera.updateProjectionMatrix();};
 const observer=new ResizeObserver(resize);observer.observe(canvas);resize();
 canvas.addEventListener('pointermove',event=>{const rect=canvas.getBoundingClientRect();targetY=((event.clientX-rect.left)/rect.width-.5)*.5;targetX=((event.clientY-rect.top)/rect.height-.5)*.35;});
 const render=()=>{if(!reduced){root.rotation.y+=(targetY-root.rotation.y)*.025;root.rotation.x+=(targetX-root.rotation.x)*.025;root.rotation.y+=.0025;wire.rotation.y-=.0015;rings.forEach((ring,index)=>ring.rotation.z+=(index%2?1:-1)*.0018);particles.rotation.y+=.00035;}renderer.render(scene,camera);if(!reduced)requestAnimationFrame(render);};
 render();
}
