from identity_app.models import User
from policy_engine.models import Policy

def Evaluate_User(user):
    return {
    "username": user.username,
    "department": user.department,
    "role": user.role,
    "experience": user.experience,
    "trust_score": user.trust_score,
    "is_active":user.is_active 
    }

    
def Evaluate_Policy(user,action,resource):

    policies=Policy.objects.filter(
        action=action,
        resource_type=resource,
        is_active=True        
    )
    matched_policies =[]
    for policy in policies:
        role_match=user.role in policy.conditions.get('allowed_roles',[])
        dept_match=user.department in policy.conditions.get('departments',[])
        trust_match=user.trust_score >=getattr(policy,'min_trust_score',0)
        if role_match and dept_match and trust_match:
            matched_policies.append({
                "policy": policy,
                "result":policy.effect,
                "reason":f"{policy.policy_name} -{policy.effect} to {policy.action} on {policy.resource_type}"
            })
        
    if not matched_policies:
        return {"result":"deny","reason":"No policy matched with user's action/resource "}

    
    matched_policies.sort(key = lambda p: p['policy'].priority,reverse=True)
    winner=matched_policies[0]
        
    return winner        