"use client"
import { useEffect } from "react";
import articles from "./Dailyscrap_selenium.json";

export default function Home() {
  const extracted = articles["Extracted datas"].data;
  const articles_data = extracted.slice(0, 4);

  useEffect(() => {
    console.log(articles_data);
  }, [articles_data]);

  return (
    <div className="h-screen w-screen flex flex-col justify-start items-center">
      <div className="flex flex-col space-y-4 items-center justify-center">
        <span className="text-5xl font-bold">DailyKorben</span>
        <span className="text-md mb-8">Les 4 infos du jour</span>
      </div>
      <ul className="w-1/2 h-auto space-y-4">
        {articles_data.map((article, index) => (
          <li key={index} className="p-4 border rounded">
            <h2 className="font-semibold text-lg">{article['data']}</h2>
          </li>
        ))}
      </ul>
    </div>
  );
}