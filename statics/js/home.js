$(document).ready(function () {
    const a_cardList = ["#a-listedFiles", "#a-transfers", "#a-setting"]
    const cardList = ["#listedFiles", "#transfers", "#setting"]
    $("#a-listedFiles").click(() => {
        for (let i = 0; i < cardList.length; i++) {
            $(cardList[i]).css("display", "none");
            $(a_cardList[i]).addClass("link-dark");
        }
        $("#a-listedFiles").removeClass("link-dark").addClass("link-secondary");
        $("#listedFiles").css("display", "flex");
    });
    $("#a-transfers").click(() => {
        for (let i = 0; i < cardList.length; i++) {
            $(cardList[i]).css("display", "none");
            $(a_cardList[i]).addClass("link-dark");
        }
        $("#a-transfers").removeClass("link-dark").addClass("link-secondary");
        $("#transfers").css("display", "flex");
    });
    $("#a-setting").click(() => {
        for (let i = 0; i < cardList.length; i++) {
            $(cardList[i]).css("display", "none");
            $(a_cardList[i]).addClass("link-dark");
        }
        $("#a-setting").removeClass("link-dark").addClass("link-secondary");
        $("#setting").css("display", "flex");
    });
    $("#logout").click(() => {
        request({
            name: "logout",
            success: (res) => {
                200 === res.data.code && 200 === res.status ? (
                    window.location.replace("/login/")
                ) : (
                    console.log(res.data.result.msg)
                );
            },
        });
    });
    let sign;
    $("#qrcode").click(() => {
        request({
            name: "qrcode",
            success: (res) => {
                let img_url = undefined;
                if (200 === res.data.code && 200 === res.status) {
                    sign = res.data.result.sign;
                    imgurl = "/api/dupan/login/qrcodebytes?sign=" + res.data.result.sign;
                    $("#qrcode img").attr("src", imgurl);
                }
            }
        });
    });
    $("#is_login").click(() => {
        request({
            name: "is_login",
            data: {sign: sign},
            success: (res) => {
                if (res.data.code === 200) {

                } else {

                }
            }
        });
    });
});
