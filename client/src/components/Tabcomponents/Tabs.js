import React, {useState} from "react";
import "./Tabs.css"

import TabNavItem from "./TabNavItem";
import TabContent from "./TabContent";

import BronxTab from "./BronxTab";
import BrooklynTab from "./BrooklynTab";
import ManhattanTab from "./ManhattanTab";
import QueensTab from "./QueensTab";
import StatenIslandTab from "./StatenIslandTab";




    function Tabs ({skateparkdata}) {

        const [activeTab, setActiveTab] = useState("tab1");

        const bronxParks = skateparkdata.filter(skatepark => skatepark.borough === "Bronx");
        const brooklynParks = skateparkdata.filter(skatepark => skatepark.borough === "Brooklyn");
        const manhattanParks = skateparkdata.filter(skatepark => skatepark.borough === "Manhattan");
        const queensParks = skateparkdata.filter(skatepark => skatepark.borough === "Queens");
        const statenislandParks = skateparkdata.filter(skatepark => skatepark.borough === "Staten Island");




        return (
            <div className="Tabs">
                <ul className="nav">
                    <TabNavItem title="Bronx" id="tab1" activeTab={activeTab} setActiveTab={setActiveTab}/>
                    <TabNavItem title="Brooklyn" id="tab2" activeTab={activeTab} setActiveTab={setActiveTab}/>
                    <TabNavItem title="Manhattan" id="tab3" activeTab={activeTab} setActiveTab={setActiveTab}/>
                    <TabNavItem title="Queens" id="tab4" activeTab={activeTab} setActiveTab={setActiveTab}/>
                    <TabNavItem title="Staten Island" id="tab5" activeTab={activeTab} setActiveTab={setActiveTab}/>

    
                </ul>
            <div className="outlet">
                <TabContent id="tab1" activeTab={activeTab}>
                <BronxTab bronxParks={bronxParks}/>
                </TabContent>
                <TabContent id="tab2" activeTab={activeTab}>
                <BrooklynTab brooklynParks={brooklynParks}/>
                </TabContent>
                <TabContent id="tab3" activeTab={activeTab}>
                <ManhattanTab manhattanParks={manhattanParks}/>
                </TabContent>
                <TabContent id="tab4" activeTab={activeTab}>
                <QueensTab queensParks={queensParks}/>
                </TabContent>
                <TabContent id="tab5" activeTab={activeTab}>
                <StatenIslandTab statenislandParks={statenislandParks}/>
                </TabContent>
            </div>
            </div>
        );
    };

export default Tabs;