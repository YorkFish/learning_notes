/* window 是 JS 中最大的对象，代表窗口
    on     当 ... 的时候
    onload 当页面加载完成之后
*/
window.onload = function(){
    // 通过元素的 id 属性获取元素对象
    var oDiv = document.getElementById('item1');
    console.log("oDiv =", oDiv);
};

