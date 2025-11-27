import axios from "axios";
import { HttpsProxyAgent } from "https-proxy-agent";
const PROXY_URL = "http://xbpjrdsx:bkp9e90grfyk@142.111.48.253:7030";
const agent = new HttpsProxyAgent(PROXY_URL);
// Utility: extract clean video ID
export function getVideoId(url) {
  try {
    const u = new URL(url);
    if (u.hostname.includes("youtu.be")) return u.pathname.slice(1);
    if (u.hostname.includes("youtube.com")) return u.searchParams.get("v");
    return url;
  } catch (e) {
    return url;
  }
}

export function getPlaylistId(url) {
  try {
    const u = new URL(url);
    return u.searchParams.get("list");
  } catch (e) {
    return null;
  }
}

// ANDROID CLIENT
const ANDROID_CLIENT = {
  context: {
    client: {
      clientName: "ANDROID",
      clientVersion: "19.09.37",
      androidSdkVersion: 33,
      osVersion: "13",
      platform: "MOBILE",
      hl: "en",
      gl: "US",
    },
  },
};

const WEB_CLIENT = {
  context: {
    client: {
      clientName: "WEB",
      clientVersion: "2.20241203.01.00",
      hl: "en",
      gl: "US",
    }
  }
};
const WEB_KEY = "AIzaSyB-4-0aQ_nu0Y-T9yg2FH44GUnuKc6PpYA";


const ANDROID_KEY = "AIzaSyAO_FJ2MiFh2wKxxDNIeEYx6HQj-DR8P9A";

// 🔥 Your Webshare Proxy
const PROXY = {
  host: "142.111.67.146",
  port: 5611,
  auth: {
    username: "xbpjrdsx",
    password: "bkp9e90grfyk",
  },
};
export async function fetchTranscript(videoId, lang = "en") {
  try {
    const playerRes = await axios.post(
      `https://www.youtube.com/youtubei/v1/player?key=${WEB_KEY}`,
      { ...WEB_CLIENT, videoId},
      {
        // headers: {
        //   "User-Agent": "com.google.android.youtube/19.09.37 (Linux; U; Android 13)",
        // },
        httpsAgent: agent,   // 🔥 FIX
      }
    );

    const tracks =
      playerRes.data?.captions?.playerCaptionsTracklistRenderer?.captionTracks;

    if (!tracks) return { error: "No captions" };

    const track = tracks.find(t => t.languageCode === lang) || tracks[0];

    const xmlUrl = track.baseUrl.replace("fmt=json3", "fmt=srv3");

    const captionRes = await axios.get(xmlUrl, {
      httpsAgent: agent,   // 🔥 FIX
    });

    return captionRes.data;

  } catch (e) {
    return { error: e.message };
  }
}