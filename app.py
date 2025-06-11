import streamlit as st

# Example data using Markdown-formatted summaries
transcripts_data = {
    "Sample 1": {
        "transcript": """
[Speaker:0] Good morning. Thank you for calling second Auto Control. This is Sam speaking. How can I direct your call?

[Speaker:1] Hey. Good morning. I would like to talk to, check the call support for a cooler panel.

[Speaker:0] Sure thing. Give me just a moment while I transfer you.

[Speaker:1] Awesome. Thank you.

[Speaker:0] You're welcome.

[Speaker:2] Morning. Tony speaking. How may I help you?

[Speaker:1] Hey, Tony. This is Chase with RSP Supply. How are you? Great. Thanks. How about yourself? Doing pretty good. Hey. I just wanted to, I'm looking for a cooler panel for a model Saginaw model o c five seven two six. And I got the serial number for you.

[Speaker:2] Pulling up an o c five seven two six at all on our system.

[Speaker:1] Okay. Yeah. I wasn't pulling it up either. I was just trying to help a customer out a customer out, but they might have the wrong model.

[Speaker:2] Right. Okay. Yeah. And that I I couldn't search it by a serial number because we don't have anything like that. That might be a ciphered part. It's not pulling up.

[Speaker:1] Oh, okay. Gotcha. Alright. I'll get back with them and see if I can get a actual model number. I appreciate your time. Sorry about

[Speaker:2] Those those have stickers on them. If you took a sticker of it or a picture of the sticker, we could help you find it too. Okay. If it was if it was our AC unit, it would have an SD sticker and then a part number on that that would be ours. So then we'll be able to help you figure that out for you.

[Speaker:1] Sounds good. Thank you, man. I appreciate it.

[Speaker:2] You're welcome. Hey. No problem. Have good day. You

[Speaker:1] too. Bye. Bye.
""",
        "summary_1": """
## Call Summary with Chase from RSP Supply

Spoke with **Chase from RSP Supply** — super polite, sounded like he was just trying to help a customer out quickly. Call was short and easy, mostly just a part lookup with no immediate resolution.

---

### What Came Up
Chase was looking for a **cooler panel** for a **Saginaw model OC5726**. He also had a **serial number** ready, hoping that might help locate the part. Unfortunately, that model number wasn’t pulling up on our end either, and I let him know we don’t have the capability to search by serial number alone.

---

### Challenges or Pain Points
- Main issue appears to be a **bad or incomplete model number**.
- Chase mentioned the **customer might’ve provided incorrect info**.
- Chase is likely **not the end user**, just facilitating the request on someone else’s behalf.

---

### Technical Notes
- Informed Chase that if the unit is ours, it would have an **SD sticker and a part number** on it.
- Suggested he send a **photo of the sticker**, which would help track it down.
- He seemed **appreciative** of the information.

---

### Action Items
- **No immediate action** on our end.
- Chase will check back with his customer to get a more **accurate model number or a picture** of the equipment label.

---

### Follow-up Timing
- **Nothing scheduled** yet.
- We might hear back from Chase once he has **better information**.
- This felt more like a **quick recon call** than a final request.

---

### Takeaways
- Chase seems like a **good contact**—professional, to the point, and respectful of our time.
- If we help him get this sorted, he’ll likely **remember the support**.
- **Potential relationship opportunity** with RSP if they need more parts down the line.

---

### Relationship Notes
- Nothing personal came up.
- Chase sounded like someone **used to working with tech support**.
- He knew what info to provide and **didn’t waste time**.
- **Easy to talk to**, and his tone/approach would be **recognizable in future calls**.

---

### Summary
This was a **quick call** to help a distributor with a **potentially misidentified part**. If Chase gets back to us with better info, we’ll likely be able to help. **Keep the door open** with RSP—there could be more opportunities, and Chase is a **solid contact** to stay in touch with.

""",
        "summary_2": """
# Call Summary

**Customer Name:** Dwayne  
**Company:** RSP Supply  
**Representative:** Chase  

## Purpose of Call
Dwayne called to confirm product details before making a purchase online. He found RSP Supply through a parts search.

## Key Points
- Dwayne created an account and wants to purchase a Lovato breaker (Part #: **P1MB2PC20**).
- The website indicates the item must be purchased in **packs of six**.
- Chase confirmed the price is **$84.40 per unit**, and full packs must be ordered (no splitting).
- Dwayne only needs **three units**, but understands he must buy six due to the pack requirement.
- He mentioned he can likely place the order using a **P-Card** and is considering **next-day delivery**.
- Dwayne will clarify internally and likely complete the purchase through the online store.

## Outcome
Dwayne thanked Chase for the help and said he would place the order online after confirming a few things on his end.

"""
    },
    "Sample 2": {
        "transcript": """
[Speaker:0] Hi. This is Grant with RSP Supply. How can I help you?

[Speaker:1] Hey. Hey. Hi. This is Reggie. I would like to check the stock of an item that I'm looking on your page where, please.

[Speaker:0] Okay. And what's gonna be that part number?

[Speaker:1] Part number, one zero five nine three three zero zero three zero.

[Speaker:0] Okay. I believe you actually did we speak yesterday about this part?

[Speaker:1] Yes.

[Speaker:0] Yeah. Did you not receive my email? I did send that over.

[Speaker:1] Oh, it's because I will let you check that if I place an order. Mhmm. And can I have it in four weeks? Or what what would be the or

[Speaker:0] Let me

[Speaker:1] the new lead time.

[Speaker:0] Yeah. Let me find that email. So it looks like it was about a five to seven week lead time is what I sent over to you.

[Speaker:1] Let me check.

[Speaker:0] Yeah. You had the sales sixteen at El Paso n I s dot com?

[Speaker:1] Yeah.

[Speaker:0] That was your email. Correct? Yeah. I did send that over.

[Speaker:1] Let me check. It's because I have I shared my email with another two person. So sometimes they close my email.

[Speaker:0] Yep. Yeah. It would've come from Grant Smith. Grants dot Smith at RSP Supply dot com.

[Speaker:1] Oh, yes. I'm looking an estimate five to seven weeks lead time.

[Speaker:0] Mhmm.

[Speaker:1] Okay. Sounds good. Thank you so much. And, if I would like to purchase, I have to do it through the website, or I have to copy on my email?

[Speaker:0] Yeah. So you can either if we have I believe you guys purchased us before, if I'm not mistaken, but you can purchase from the website. Or if you wanna call in, we can get you an official quote for that. A lot of these regular parts do have a small tariff on them, just so you're aware.

[Speaker:1] Oh, okay. Okay. Sounds good. Thank you so much. Thank you. I'm so sorry for that.

[Speaker:0] No. You're out. It's fun to make sure you got it. Of course. Have a good rest of your day.

[Speaker:1] No. No. No. Thank you so much. I have it in my email. Thank you. Have a good one.

[Speaker:0] Of course. You too. Bye bye.

[Speaker:1] Thank you.
""",
        "summary_1": """
## Spoke with Reggie

Very polite and easygoing guy. Just a quick follow-up call to confirm a part's availability and lead time. Sounded like he was double-checking before placing an order, likely just being thorough on his end.

---

### **Product Status**

He was calling about part number **1059330030**, which we had discussed yesterday. I had already sent him the lead time info via email, but he hadn’t seen it yet — turns out he shares that inbox with a couple of other people, so things sometimes get closed out before he sees them. Once I reminded him of the email (from **Grant.Smith@RSPSupply.com**), he pulled it up while we were on the call and confirmed he now sees the **5–7 week lead time** I quoted.

---

### **What Came Up**

He wanted to know if it was possible to receive the part within **four weeks**.  
I let him know again that unfortunately, it’s showing as a **5–7 week lead time** currently.  
He was okay with that — didn’t push back, just wanted to confirm before ordering.

---

### **Ordering Process**

He asked if he needs to place the order through the website or if **email is okay**.  
I let him know both are fine — they’ve purchased from us before, so he can either order online or call in if he wants a **formal quote**.  
I also gave him a heads-up about the **small tariff** on this part, which he appreciated.

---

### **Tone & Personality**

Super friendly and respectful.  
He apologized a couple of times for missing the email, and I reassured him it’s no problem — just wanted to make sure he had the info he needed.  
Very cooperative and appreciative throughout.

---

### **Action Items**

No immediate action needed from our end.  
He now has the lead time info and ordering options, so the ball’s in his court if/when he’s ready to purchase.

---

### **Follow-up Timing**

No follow-up needed unless we hear back from him with an order or additional questions.  
He now knows how to proceed.

---

### **Takeaways**

Reggie seems **detail-oriented** and wants to be sure of timelines before committing to a purchase.  
Might be coordinating with others based on how he mentioned sharing the email inbox.  
Worth keeping in mind that future communications may get missed unless they’re flagged clearly or followed up with a quick call.

---

### **Relationship Notes**

Nothing personal came up this time, but his tone and manner suggest he’s someone who values **good customer service** and **clear info**.  
A pleasant contact to deal with — if he orders again, we should be ready to provide **fast updates** and keep things **simple**.

---

### **Summary**

Good touchpoint with Reggie.  
Just a confirmation call, but it helped ensure he had the info in hand.  
Sounds like there’s a decent chance he’ll place an order once he confirms the lead time works for him and his team.  
**Definitely a warm lead.**

""",
        "summary_2": """
## Call Summary

- **Customer:** Reggie  
- **Company:** RSP Supply  
- **Purpose of Call:** Check stock and lead time for part number **1059330030**

### Key Points:

- Grant (RSP Supply) confirmed they had spoken the previous day and that he had already sent the lead time via email.
- Reggie mentioned he shares his email inbox, so the message might have been overlooked.
- Grant verified the email address and reiterated that the **lead time is 5 to 7 weeks**.
- Reggie inquired about how to place an order.
  - Grant explained that Reggie could:
    - Order through the website, or  
    - Call in to request an official quote  
  - Note: Some parts may include a **small tariff**.
- The call concluded with Reggie confirming he had located the email and thanking Grant.

"""
    },
    "Sample 3": {
        "transcript": """
[Speaker:0] Thank you for calling RSP. This is Chase. How can I assist?

[Speaker:1] Hi, Chase. My name is Rebecca, and I'm looking for a Dwyer part, a quantity of two. And I've got a part number. I wondered if you could tell me if you have it.

[Speaker:0] Yeah. Sure thing. What's the part number?

[Speaker:1] Okay. It's Victor alpha two zero four three four.

[Speaker:0] Alrighty. And so you're looking for two of them?

[Speaker:1] Yes.

[Speaker:0] Okay. Let's see. Okay. Just while I'm looking this up, what's your timeline on this?

[Speaker:1] I'm looking for it to be in stock. And if it is, then I'm gonna place an order.

[Speaker:0] Gotcha. Okay. Alrighty. Okay. So it's looking like so I don't have it in stock in my Salt Lake City warehouse, but I have a couple more warehouses around the country. I got one in California. I also have one in Idaho. So let me reach out to them real quick to verify availability there. And then do you mind if I shoot you over an email with an update when I have a good answer for you?

[Speaker:1] Yeah. What's your email address? And I'll send you my contact information.

[Speaker:0] Yeah. It's, chase, c h a s e, dot fisher, s I s h e r, at r s p r s p supply dot com. Okay.

[Speaker:1] Alright. I just sent you an email. So if you find something out, let me know, please.

[Speaker:0] Perfect. Absolutely. Will do. Thanks, Jay. Of course.

[Speaker:1] Bye.
""",
        "summary_1": """
## Spoke with Rebecca

Rebecca was direct, polite, and clearly knew what she was after. She just needed help sourcing a specific Dwyer part and wanted to move quickly if we had it.

---

### **Product Status**

Rebecca was looking for a Dwyer part, **VA20434**, quantity **two**. I checked availability in our **Salt Lake City** warehouse, but we didn’t have any in stock there. I let her know I’d reach out to a couple of our other locations — specifically in **California** and **Idaho** — to see if they had stock.

---

### **What Came Up**

Timeline-wise, she’s ready to place an order **immediately** if the part is available. No mention of a broader project or order — this was clearly a **quick-turn request**, but the speed and decisiveness suggest she might be handling procurement for something **time-sensitive**.

---

### **Action Items**

- I told her I’d confirm availability with our other warehouses and follow up by email.  
- She asked for my email address and said she’d send over her contact info — which she did within the call.

---

### **Follow-up Timing**

As soon as I hear back from the **CA** or **ID** warehouse teams, I’ll need to email her right away.  
This is clearly a **“whoever gets it first gets the order”** situation.

---

### **Takeaways**

- Rebecca didn’t say much about what the part was for, but she had the part number ready and was efficient — probably handles purchasing regularly.
- Good potential for **future spot buys** if we come through on this one.

---

### **Relationship Notes**

- Nothing personal came up, but she was **pleasant and responsive**.
- No hesitation in sending over her contact info — definitely open to doing business.

---

### **Looking Ahead**

If we can deliver on this request fast, it’s worth keeping her info handy.  
Could be a solid **repeat buyer** for specialty parts or rush orders.  
Would be smart to ask next time what kind of **projects or systems** she typically sources for.

""",
        "summary_2": """
# Call Summary

**Customer Name:** Rebecca  
**Representative:** Chase (RSP)  

## Purpose of Call
Rebecca inquired about the availability of a Dwyer part (**Part #: VA20434**) and requested a quantity of two.

## Key Points
- Rebecca wants to place an order **only if the parts are in stock**.
- Chase checked the **Salt Lake City warehouse** — **not in stock**.
- Chase will check availability in other warehouses (**California and Idaho**).
- Rebecca provided her contact info via **email**.
- Chase will **follow up via email** once he confirms availability.

## Next Step
Chase to email Rebecca with stock status from other warehouses.

"""
    }
}

# Streamlit layout
st.set_page_config(page_title="Transcript Summary Comparator", layout="wide")
st.title("📞 Transcript Summary Comparator")

# Group selection
group = st.selectbox("Select a group to compare:", list(transcripts_data.keys()))
data = transcripts_data[group]

# Display transcript
st.subheader(f"Call Transcript - {group}")
st.markdown(f"📄 **Transcript:**\n\n{data['transcript']}")

# Show summaries in columns
st.markdown("### 📊 Summary Options Comparison")
col1, col2 = st.columns(2)

with col1:
    st.markdown("**Justin's Summary**")
    st.markdown(data['summary_1'])

with col2:
    st.markdown("**Current Browser Extension Summary**")
    st.markdown(data['summary_2'])

# & "C:/Users/Pedro Sanhueza/AppData/Local/Programs/Python/Python313/Scripts/streamlit.exe" run "C:/Users/Pedro Sanhueza/OneDrive - RSP Supply/Documents/Script/Platforms/Streamlit/Quick - Prompt comparisson/app.py"
