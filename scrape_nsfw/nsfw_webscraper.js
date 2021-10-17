const puppeteer = require('puppeteer');
const fs = require('fs');

const scrapeUser = async ()=>{
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    let data = [];
    try{
        for(let i = 1; i < 1061; i++){
            console.log(i);
            await page.goto(`https://chaturbot.co/reddit_nsfw_index?page=${i}`);
            await page.content();
            let list_of_nsfw = await page.$$eval('tbody > tr > td.name > div.name', (nsfw_subs)=>{
                let sad = [];
                for(let i of nsfw_subs)sad.push(i.querySelector('a').innerText)
                return sad
            })
            data.push(...list_of_nsfw.map(e=>({nsfw: e})));
        }

        const finished_list = data.map(JSON.stringify).join('\n');

        fs.writeFile('nsfw_subs.json', finished_list, (err)=>{
            if (err) console.log('an error occured while saving', err);
            else console.log('data saved');
        });

        
        await page.close();
        await browser.close();
    }
    catch(err){
        //console.log('an error occured\n', err);
        await page.close();
        await browser.close();
    }
}

scrapeUser();