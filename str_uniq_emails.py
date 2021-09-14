class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniq_emails = set()
        for email in emails:
            host,domain = email.split('@')
            if '+' in host:
                host = host[:host.index('+')]
            uniq_emails.add(host.replace('.','') + '@' + domain)
        return len(uniq_emails)
