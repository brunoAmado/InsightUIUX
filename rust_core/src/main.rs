use std::env;

/// Strips zero-width and Trojan-Source bidirectional override characters (CVE-2021-42574).
pub fn strip_steganographic_unicode(input: &str) -> (String, usize) {
    let mut cleaned = String::with_capacity(input.len());
    let mut removed = 0usize;
    for ch in input.chars() {
        let code = ch as u32;
        let is_steg = (0x200B..=0x200F).contains(&code)
            || (0x202A..=0x202E).contains(&code)
            || (0x2060..=0x2069).contains(&code)
            || code == 0xFEFF
            || (0xE0000..=0xE007F).contains(&code);
        if is_steg {
            removed += 1;
        } else {
            cleaned.push(ch);
        }
    }
    (cleaned, removed)
}

/// Computes the exact Concentric Border Radius (R_outer = R_inner + padding).
pub fn compute_concentric_outer_radius_px(inner_radius_px: u32, padding_px: u32) -> u32 {
    inner_radius_px.saturating_add(padding_px)
}

/// Deterministic 64-bit FNV-1a fingerprint for UI/UX design token caching.
pub fn fnv1a_64(input: &str) -> u64 {
    let mut hash: u64 = 0xcbf29ce484222325;
    for b in input.as_bytes() {
        hash ^= *b as u64;
        hash = hash.wrapping_mul(0x100000001b3);
    }
    hash
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let sample = args.get(1).map(|s| s.as_str()).unwrap_or("InsightUIUX");
    let (cleaned, removed) = strip_steganographic_unicode(sample);
    let fp = fnv1a_64(&cleaned);
    let outer_r = compute_concentric_outer_radius_px(8, 8);
    println!(
        "{{\"member\":\"InsightUIUX\",\"cleaned\":\"{}\",\"steganographic_removed\":{},\"concentric_outer_radius_px\":{},\"fnv1a_64\":\"0x{:016x}\"}}",
        cleaned, removed, outer_r, fp
    );
}
