gsap.to(
    ".logo", 
    {
		delay: 1,
		duration: 2, 
        x: 300, 
		y: 300,

        backgroundColor:"#560563", 
        borderRadius: "20%", 
        border:"5px solid aqua", 
        ease:"back",
		skewY: 45,
    });
 
    gsap.to(".box", {rotation: 27, x: 100, duration: 1, });

var obj = {prop: 10};
gsap.to(obj, {
  duration: 1,
  prop: 200, 
  //onUpdate fires each time the tween updates; we'll explain callbacks later.
  onUpdate: function() {
    console.log(obj.prop); //logs the value on each update.
  },
  onComplete: function() {
    console.log("FIN");  
  }
});