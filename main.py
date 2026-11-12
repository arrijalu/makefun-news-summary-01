# -*- coding: utf-8 -*-
"""
main.py - News Summary Generator for 11 November 2026
"""
import os
import sys

def generate_summary():
    facts = [
        # 1. Trilateral talks & Russia ceasefire rejection
        "US Secretary of State Marco Rubio called trilateral US-Russia-Ukraine talks in Abu Dhabi 'very productive'; Russia rejected European ceasefire proposals. (AA/APEX)",
        # 2. Iran war
        "After meeting Qatar's PM, President Trump said the war with Iran is 'militarily effectively over'. (AP/NPR)",
        # 3. Venezuela protectorate
        "A year after US forces ousted Nicolas Maduro, Venezuela has become a US protectorate. (NYT)",
        # 4. COP31 summit opening
        "The COP31 UN climate summit opened in Antalya, Turkiye; Turkiye seeks to raise electricity's share of global energy to 35% by 2035; President Erdogan and UN chief Guterres spoke. (Anadolu/AA)",
        # 5. COP31 Gaza
        "At COP31 Erdogan called Israel's war in Gaza an 'ecocide' and urged Israel to let aid in. (AP)",
        # 6. China trade surplus
        "China's trade surplus passed $1.04 trillion in the first ten months of 2026, a record; October exports exceeded imports by $105.3 billion. (NYT)",
        # 7. Gen Z protests
        "Gen Z-led protests spread across several countries, described as a global political awakening. (NYT)",
        # 8. German deindustrialisation
        "German towns faced auto-sector layoffs and plant cutbacks, deepening deindustrialisation fears. (AA)",
        # 9. House Hegseth impeachment
        "The House voted 211-204 to send an impeachment resolution against Defense Secretary Pete Hegseth to committee, killing it. (AA)",
        # 10. Trump BBC suit
        "A US judge let Trump's defamation suit against the BBC proceed, dropped one claim, and ordered his deposition by 11 December. (AP)",
        # 11. Brazil Facebook fine
        "A Brazilian court fined Facebook $1.3 million for failing to comply with orders during the election. (AP)",
        # 12. US beef prices
        "US beef prices hit records as the cattle herd fell to its smallest level in 75 years. (WSJ)",
        # 13. Pope Leo Argentina visit
        "Pope Leo ended an Argentina visit with a Mass for about two million people and left for Peru, his second homeland. (AP)",
        # 14. Darchiev death
        "Russia's ambassador to the United States, Alexander Darchiev, died at 66. (AP)",
        # 15. Atacama desert bloom
        "Rare rains turned about 7,000 square miles of Chile's Atacama Desert into its biggest wildflower bloom in decades. (NPR)"
    ]

    header = "GLOBAL NEWS SUMMARY BRIEFING -- WEDNESDAY, 11 NOVEMBER 2026\n\n"
    body = "\n\n".join(f"{i+1}. {fact}" for i, fact in enumerate(facts))
    footer = "\n\n[End of Global News Briefing -- 11 November 2026]"
    
    return header + body + footer

def main():
    summary_text = generate_summary()
    encoded = summary_text.encode('ascii')
    byte_count = len(encoded)
    
    print(f"Generated summary byte count: {byte_count}")
    if not (1900 <= byte_count <= 1999):
        print(f"ERROR: Byte count {byte_count} out of range [1900, 1999]", file=sys.stderr)
        sys.exit(1)
        
    os.makedirs("output", exist_ok=True)
    
    with open("entry.txt", "wb") as f:
        f.write(encoded)
        
    with open("output/entry.txt", "wb") as f:
        f.write(encoded)
        
    print("Successfully wrote summary to entry.txt and output/entry.txt")

if __name__ == "__main__":
    main()
