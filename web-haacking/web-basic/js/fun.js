// closure
let a=1000
function fun(){
  // let a=10;
  return ()=> console.log(a)
}

var closure =fun()
closure()


// Event Listner
// {
//   let click_count =0;
 
// document.getElementById("btn").
// addEventListener("click",function(){
//     click_count+=1;
//     alert("button clicked "+click_count+" times");
// })
// }
// click_count =99;
// console.log(click_count);

console.log(document.getElementById('btn'))
function attachEventListner(){
  let count =0;
  document.getElementById('btn').addEventListener('click',
    (  ()=>{ console.log("button pressed ",++count," times")
}));
}
attachEventListner();
