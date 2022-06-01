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
    $("#qrcode").click(() => {
        request({
            name: "qrcode",
            success: (res) => {
                let img_url = undefined;
                if (200 === res.data.code && 200 === res.status) {
                    imgurl = "/api/dupan/login/qrcodebytes?sign=" + res.data.result.sign;
                    $("#qrcode img").attr("src", imgurl);
                    // do {
                    //
                    // } while()
                }
            }
        });
    });
});

// 如果第一次请求，则获取二维码并执行is_login
// 如果已经执行了is_login期间点击了二维码 则停止任务并重新执行is_login

async function is_login(sign) {
    return await new Promise(resolve => {
        request({
            name: "is_login",
            data: {
                sign: defaultConfigs.sign
            },
            async: true,
            success: (res) => {
                resolve()
            }
        })
    })
}