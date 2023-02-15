import streamlit as st

def bmi_visualization(BMI):
    
    outside_expander_area = st.container()
    state = st.session_state
    with outside_expander_area:
        guage = st.empty()
    bmi_thresholds = [13, 18.5, 25, 30, 43]
    level_labels = ['심각한 저체중', '저체중','정상','과체중','비만', '심각한 비만']

    if BMI <= bmi_thresholds[0]:
        level = level_labels[0]
    elif BMI <= bmi_thresholds[1]:
        level = level_labels[1]
    elif BMI <= bmi_thresholds[2]:
        level = level_labels[2]
    elif BMI <= bmi_thresholds[3]:
        level = level_labels[3]
    elif BMI <= bmi_thresholds[4]:
        level = level_labels[4]
    else:
        level = level_labels[5]

    bmi_gauge_lower = 13 # 0 degrees
    bmi_gauge_upper = 43 # 180 degrees

    bmi_guage_range = (bmi_gauge_upper - bmi_gauge_lower)
    BMI_adjusted = BMI if (BMI >= bmi_gauge_lower and BMI <= bmi_gauge_upper) else (
        bmi_gauge_lower if BMI < bmi_gauge_lower else bmi_gauge_upper
    )
    dial_rotation = round(((BMI_adjusted - bmi_gauge_lower) / bmi_guage_range) * 180.0, 1)

    html = f"""
    <html><body>
    <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="300px" height="163px" viewBox="0 0 300 163">
    <g transform="translate(18,18)" style="font-family:arial,helvetica,sans-serif;font-size: 12px;">
        <defs>
            <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="0" refY="3.5" orient="auto">
                <polygon points="0 0, 10 3.5, 0 7"></polygon>
            </marker>
            <path id="curvetxt1" d="M-4 140 A140 140, 0, 0, 1, 284 140" style="fill: none;"></path>
            <path id="curvetxt2" d="M33 43.6 A140 140, 0, 0, 1, 280 140" style="fill: #none;"></path>
            <path id="curvetxt3" d="M95 3 A140 140, 0, 0, 1, 284 140" style="fill: #none;"></path>
            <path id="curvetxt4" d="M235.4 33 A140 140, 0, 0, 1, 284 140" style="fill: #none;"></path>
        </defs>
        <path d="M0 140 A140 140, 0, 0, 1, 280 140 L140 140 Z" fill="#bc2020"></path>
        <path d="M6.9 96.7 A140 140, 0, 0, 1, 280 140 L140 140 Z" fill="#d38888"></path>
        <path d="M12.1 83.1 A140 140, 0, 0, 1, 280 140 L140 140 Z" fill="#ffe400"></path>
        <path d="M22.6 63.8 A140 140, 0, 0, 1, 96.7 6.9 L140 140 Z" fill="#008137"></path>
        <path d="M96.7 6.9 A140 140, 0, 0, 1, 280 140 L140 140 Z" fill="#ffe400"></path>
        <path d="M169.1 3.1 A140 140, 0, 0, 1, 280 140 L140 140 Z" fill="#d38888"></path>
        <path d="M233.7 36 A140 140, 0, 0, 1, 280 140 L140 140 Z" fill="#bc2020"></path>
        <path d="M273.1 96.7 A140 140, 0, 0, 1, 280 140 L140 140 Z" fill="#8a0101"></path>
        <path d="M45 140 A90 90, 0, 0, 1, 230 140 Z" fill="#fff"></path>
        <circle cx="140" cy="140" r="5" fill="#666"></circle>

        <g style="paint-order: stroke;stroke: #fff;stroke-width: 2px;">
            <text x="25" y="111" transform="rotate(-72, 25, 111)">16</text>
            <text x="30" y="96" transform="rotate(-66, 30, 96)">17</text>
            <text x="35" y="83" transform="rotate(-57, 35, 83)">18.5</text>
            <text x="97" y="29" transform="rotate(-18, 97, 29)">25</text>
            <text x="157" y="20" transform="rotate(12, 157, 20)">30</text>
            <text x="214" y="45" transform="rotate(42, 214, 45)">35</text>
            <text x="252" y="95" transform="rotate(72, 252, 95)">40</text>
        </g>

        <g style="font-size: 14px;">
            <text><textPath xlink:href="#curvetxt1">저체중</textPath></text>
            <text><textPath xlink:href="#curvetxt2">정상</textPath></text>
            <text><textPath xlink:href="#curvetxt3">과체중</textPath></text>
            <text><textPath xlink:href="#curvetxt4">비만</textPath></text>
        </g>
        
        <line x1="140" y1="140" x2="65" y2="140" stroke="#666" stroke-width="2" marker-end="url(#arrowhead)">
            <animateTransform attributeName="transform" attributeType="XML" type="rotate" from="0 140 140" to="{dial_rotation} 140 140" dur="1s" fill="freeze" repeatCount="1"></animateTransform>
        </line>
        
        
    </g>
    </svg>
    </body></html>
    """
    # 저기 맨밑에 끼우면 됨
    # <text x="65" y="120" style="font-size: 28px;font-weight:bold;color:#000;">BMI = {BMI}</text>

    with outside_expander_area:
        import streamlit.components.v1 as components

        with guage:
            components.html(html.replace('\n',''))

        st.markdown(f"<h1 style='text-align: center; font-size: 18px'>BMI 지수 상 {level}입니다({BMI})</h1>", unsafe_allow_html=True)
        # st.caption(f'Rotation: {dial_rotation} degrees')